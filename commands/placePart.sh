# open gripper
python3 ./commands/ungrip.py

echo "ungripped"

# go to part location
python3 ./commands/move.py $1 $2 $3 $4

echo "moved source"

# close gripper (grab part)
python3 ./commands/grip.py

echo "gripped"

# move part to destination
python3 ./commands/move.py $5 $6 $7 $8

echo "moved dest"

# open gripper (let go the part)
python3 ./commands/ungrip.py

echo "ungripped"
