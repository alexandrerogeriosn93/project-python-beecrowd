def format_answer(first_value, second_value):
    answer = ""

    answer += f"{first_value:.6f} - {second_value:.6f}\n"
    answer += f"{first_value:.0f} - {second_value:.0f}\n"
    answer += f"{first_value:.1f} - {second_value:.1f}\n"
    answer += f"{first_value:.2f} - {second_value:.2f}\n"
    answer += f"{first_value:.3f} - {second_value:.3f}\n"
    answer += f"{first_value:e} - {second_value:e}\n"
    answer += f"{first_value:E} - {second_value:E}\n"
    answer += f"{first_value} - {second_value}\n"
    answer += f"{first_value} - {second_value}"

    return answer

first_value, second_value = 234.345, 45.698

print(format_answer(first_value, second_value))
