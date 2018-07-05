#!/usr/bin/env bash

for REGION in `aws ec2 describe-regions --output text | cut -f3`
do
    echo -e "\n Finding Instances in regions: '$REGION'"
    aws ec2 describe-instances --region $REGION
done