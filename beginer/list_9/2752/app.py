def format_answer(text):
    answer = ""

    answer += f"<{text}>\n"
    answer += f"<{text:>30s}>\n"
    answer += f"<{text:>.20s}>\n"
    answer += f"<{text:20s}>\n"
    answer += f"<{text:30s}>\n"
    answer += f"<{text:>.30s}>\n"
    answer += f"<{text:>30.20s}>\n"
    answer += f"<{text:30.20s}>"

    return answer

text = "AMO FAZER EXERCICIO NO URI"
print(format_answer(text))
