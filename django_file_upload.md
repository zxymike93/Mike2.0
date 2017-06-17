# File Uploads

> 在 Django 中上传文件，数据是以 `request.FILES` 来处理的。

## Basic
    #! forms.py
    from django import forms
    class UploadFileForm(forms.Form):
        somefile = forms.FileField()
    #! views.py
    def upload_file(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
            	＃ 处理 file 的三种常见方式
                -------
            	# 1. 手动制定文件写入
                handle_uploaded_file(request.FILES['somefile'])
                -------
                # 2. automatically saving file to `upload_to` with ModolForm:
                form.save()
                -------
                # 3. 利用 Model 实例化
                instance = Model(file_filed=request.FILES['somefile'])
                instance.save()
                -------
                return HttpResponseRedirect('/success/')
            else:
                form = UploadFileForm()
            return render(request, 'upload.html', {'form': form})
    #！ handle file function
    	def handle_uploaded_file(f):
        	# alike python's file.read()
            # but using File.chunks() instead
        	with open('path/to/file.txt', 'wb+') as destination:
            	for chunk in f.chunks():
                	destination.write(chunk)

## Upload Handlers
> django settings 里有个 FILE_UPLOAD_HANDLERS，默认小于 2.5MB 的文件走内存，大于则直接走硬盘临时文件（如：/tmp/tmpfile.upload）:

```py
FILE_UPLOAD_HANDLER = [
"django.core.files.uploadhandler.MemoryFileUploadHandler"，
"django.core.files.uploadhandler.TemporaryFileUploadHandler"
]
```
