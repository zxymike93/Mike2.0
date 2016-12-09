# Git 笔记
### 工作区 / 暂存区 / 分支仓库

- git diff    
查看工作区有无改动  
- git diff `file`  
查看某一文件在工作区有无改动  
- git diff HEAD -- `file`  
查看工作区的文件和指定版本的区别

- git checkout -- `filename`    
取消该工作区的改动(包括 git rm `file` 但没 commit 前)  

- git add `filename`    
加入暂存

- git reset HEAD `filename`    
从暂存退回工作区

- git commit -m "message"    
保存到仓库

- git reflog    
命令历史  
978250a HEAD@{0}: commit (initial): wrote a readme file

- git log --pretty=oneline    
提交历史  
653a7cab219d4bbd011a252a9a27688a36acb3bd add 'distributed'

- git reset --hard `HEAD` or `HEAD^` or `HEAD~100` or `653a7cab219d4`    
版本滚动  

- ssh-keygen -t rsa -C "email@example.com"  
私钥 id_rsq 公钥 id_rsa.pub 在目录 /zxy/.ssh/  
 

