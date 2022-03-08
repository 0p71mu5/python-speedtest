git pull
::echo "[i] Initializing Git"
git init
::echo "[i] Adding files"
git add .
::echo "[i] Commit git as update"
set timestamp=%date% %time%
git commit -m "%timestamp%" -a
::echo "[i] Pushing branch to github "
git push
echo "*** [i] Run this script again if you get any error while git push ***"
pause
