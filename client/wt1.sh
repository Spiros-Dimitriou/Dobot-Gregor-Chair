# grab the leg base and place it in the w1 gripper
curl --location --request POST "${R1_IP}:${R1_PORT}/placePart" \
--header 'Content-Type: application/json' \
--data-raw '{
    "x1": "85",
    "y1": "250",
    "z1": "50",
    "r1": "75",
    "x2": "200",
    "y2": "160",
    "z2": "30",
    "r2": "42"
}'

# todo: make w1 gripper grip

for i in 1 2
do
	# grab a leg and place it into the leg base
		curl --location --request POST "${R1_IP}:${R1_PORT}/placePart" \
	--header 'Content-Type: application/json' \
	--data-raw '{
		"x1": "255",
		"y1": "25",
		"z1": "10",
		"r1": "9",
		"x2": "200",
		"y2": "160",
		"z2": "30",
		"r2": "42"
	}'
	
	# todo: make w1 gripper turn to be ready for next leg
done
