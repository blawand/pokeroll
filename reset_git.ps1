# reset_git.ps1
Write-Host "WARNING: This will delete your local git history." -ForegroundColor Yellow
Remove-Item -Path .git -Recurse -Force -ErrorAction SilentlyContinue
git init
git add .
git commit -m "Initial commit for public release"
Write-Host "Git history reset. You can now add your new remote origin." -ForegroundColor Green
Write-Host "git remote add origin <your-new-repo-url>"
Write-Host "git push -u origin master"
