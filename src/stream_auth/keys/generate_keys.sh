#!/bin/sh

ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub

openssl ec -in streamkeyEC256.key -pubout -outform PEM -out streamkeyEC256.key.pub
ssh-keygen -t ecdsa -b 256 -m PEM -f streamkeyEC256.key
