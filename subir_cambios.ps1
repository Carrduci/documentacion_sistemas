$mensajeExtra = $args[0]
$tipoCommit = $args[1]

git add *
$Mensaje = git status -s -v
git commit -m "${tipoCommit}: cambio a documentacion${mensajeExtra}" -m "${Mensaje}"
git push --follow-tags origin main