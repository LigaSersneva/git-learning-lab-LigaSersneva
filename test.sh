#!/bin/bash

if grep -q "Mans gala darbs" index.html; then

echo "Tests OK"

exit 0

else

echo "Tests FAILED"

exit 1

fi