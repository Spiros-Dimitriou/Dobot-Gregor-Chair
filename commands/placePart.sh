# open gripper
python3 ./commands/ungrip.py

# go to part location
python3 ./commands/move.py $1 $2 $3 $4

# close gripper (grab part)
python3 ./commands/grip.py

# move part to destination
python3 ./commands/move.py $5 $6 $7 $8

# open gripper (let go the part)
python3 ./commands/ungrip.py
