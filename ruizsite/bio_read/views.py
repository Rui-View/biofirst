from django.shortcuts import render
from .utils import convert_to_bionic

def input_text(request):
    # 获取传递的文本内容（如果有）
    input_text = request.GET.get('text', '')  # 使用 GET 参数传递文本
    return render(request, 'bio_read/input_text.html', {'input_text': input_text})

def show_bionic_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')  # 获取用户输入的文本
        bionic_text = convert_to_bionic(text)  # 调用函数处理文本

        return render(request, 'bio_read/result.html', {'bionic_text': bionic_text, 'original_text': text})
    else:
        return render(request, 'bio_read/input_text.html')


