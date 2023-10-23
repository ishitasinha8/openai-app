import numpy as np
import openai

# openai.api_type = 'azure'
# openai.api_version = '2022-12-01'
deployment_name = 'ishita-davinci-test-3'

# openai.api_key = "39cdcddc7d15446c8588a34eada4d121"
# openai.api_base = "https://testnew.openai.azure.com/"


def split_files_into_groups(files, group_size):
    file_groups = []
    group_count = len(files) // group_size

    for i in range(group_count):
        group_start = i * group_size
        group_end = group_start + group_size
        group_files = files[group_start:group_end]
        file_groups.append(group_files)

    remaining_files = len(files) % group_size
    if remaining_files > 0:
        remaining_start = group_count * group_size
        remaining_files = files[remaining_start:]
        file_groups.append(remaining_files)

    return file_groups

def summarize_text(text_to_summarize):
    words = text_to_summarize.split(" ")
    split_len = len(words) // 3000 + 1
    chunks = np.array_split(words, split_len)
    summary_responses = []

    for chunk in chunks:
        sentences = ' '.join(list(chunk))
        prompt = f"Below are weekly status reports for Project name. Extract the key project completion trends, key changes between each, key risks, key Project Financial Summary trends (if present): #Start of Report{sentences}#End of Report"
        response = openai.Completion.create(
            engine=deployment_name,
            prompt=prompt,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=1
        )
        response_text = response["choices"][0]["text"]
        summary_responses.append(response_text)
    
    return ' '.join(summary_responses)

def generate_final_summary(text_to_summarize2_list):
    final_summary = ""
    i = 1
    less_than_three_files_summary = ''
    for text in text_to_summarize2_list:
        less_than_three_files_summary = summary = summarize_text(text)
        final_summary += "Start of Report " + str(i) + '\n'
        i += 1
        final_summary += summary + '\n'

    if len(text_to_summarize2_list) > 1:
        words = final_summary.split(" ")
        split_len = len(words) // 3000 + 1
        chunks = np.array_split(words, split_len)
        summary_responses = []

        for chunk in chunks:
            sentences = ' '.join(list(chunk))
            prompt = f"Below are status reports. Extract the key project completion trends, key changes between each, key risks, key Project Financial Summary trends: {sentences}#End of Report. Summary: "
            response = openai.Completion.create(
                engine=deployment_name,
                prompt=prompt,
                temperature=1,
                max_tokens=380,
                top_p=0.5,
                frequency_penalty=0,
                presence_penalty=0,
                best_of=1,
                stop=None
            )

            response_text = response["choices"][0]["text"]
            summary_responses.append(response_text)

        return '\n'.join(summary_responses)
    else:
        return less_than_three_files_summary
