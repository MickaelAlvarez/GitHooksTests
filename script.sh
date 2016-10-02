git reset HEAD~2
echo "un truc ce passe ?"
#on refactor en dur pour le test
echo "second_line" > f
echo "second line +bl_nouveau" >> f
git add f

git commit -m "edition after refactor2"
git push --no-verify
