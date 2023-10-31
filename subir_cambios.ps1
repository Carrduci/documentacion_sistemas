git add *
$Mensaje = git status -s -v
git commit -m "cambio a documentacion" -m "${Mensaje}"
git push --follow-tags origin main