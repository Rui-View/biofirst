def convert_to_bionic(text):
    """
    将文本转换为 Bionic Reading 格式，同时保留段落和缩进
    """
    lines = text.splitlines()  # 按行分割文本
    bionic_lines = []

    for line in lines:
        words = line.split()
        bionic_words = []

        for word in words:
            # 高亮单词前半部分
            split_index = max(1, len(word) // 2)
            highlighted = f"<strong>{word[:split_index]}</strong>{word[split_index:]}"
            bionic_words.append(highlighted)

        # 拼接当前行的 Bionic 文本
        bionic_lines.append(" ".join(bionic_words))

    # 保留原始段落和缩进
    return "\n".join(bionic_lines)
