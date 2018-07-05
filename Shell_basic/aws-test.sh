#!/usr/bin/env bash

AWS_GET_SNS=`aws sns list-subscriptions --output table`             # 得用` 符号，在Ecs按键下面
AWS_GET_EC2_REGIONS=`aws ec2 describe-regions --output json`
AWS_GET_SEQ_QUEUE=`aws sqs list-queues --output table`

echo ${AWS_GET_SNS}
echo
echo ${AWS_GET_EC2_REGIONS}
echo
echo ${AWS_GET_SEQ_QUEUE}
echo