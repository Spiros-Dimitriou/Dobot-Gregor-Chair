# open gripper
curl --location --request GET '150.140.188.191:8080/ungrip';

# go to part location
curl --location --request POST '150.140.188.191:8080/move' \
--header 'Content-Type: application/json' \
--data-raw '{
    "x": "$1",
    "y": "$2",
    "z": "$3",
    "r": "$4"
}';

# close gripper (grab part)
curl --location --request GET '150.140.188.191:8080/grip';

# move part to destination
curl --location --request POST '150.140.188.191:8080/move' \
--header 'Content-Type: application/json' \
--data-raw '{
    "x": "$5",
    "y": "$6",
    "z": "$7",
    "r": "$8"
}';

# open gripper (let go the part)
curl --location --request GET '150.140.188.191:8080/ungrip';
