from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

import json


from .models import Message ,Users
from .serializers import MessageSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_messages(request):
    """" get all messages by the receiver email """
    try:
        # json_data = json.loads(request.body)
        # msgs_list = Message.objects.filter(reciever=json_data['email'])
        myuser = Users.EMAIL_FIELD
        msgs_list = Message.objects.filter(reciever=myuser)
        if not msgs_list:
            return HttpResponse('There are no messages for this email address')
            # return Response(data="There are no messages for this email address")
        serializer = MessageSerializer(msgs_list, many=True)
        return HttpResponse(json.dumps(serializer.data), content_type='application/json')
        # return Response(json.dumps(serializer.data), content_type='application/json')
    except Exception:
        return {"error": "check the request, something went wrong!!!"}


@api_view(['GET'])
def get_all_unread_messages(request):
    """" get all unread messages by the receiver email """
    try:
        json_data = json.loads(request.body)
        msgs_list = Message.objects.filter(reciever=json_data['email'], is_read=False)
        if not msgs_list:
            return HttpResponse('There are no messages for this email')
        serializer = MessageSerializer(msgs_list, many=True)
        return HttpResponse(json.dumps(serializer.data), content_type='application/json')
    except Exception:
        return {"error": "check the request, something went wrong!!!"}


@api_view(['GET'])
def get_message(request):
    """" get the message by the id """
    try:
        json_data = json.loads(request.body)
        msgs_list = Message.objects.filter(reciever=json_data['email'], id=json_data['id'])
        if not msgs_list:
            return HttpResponse('There are no message with this id')
        for msg in msgs_list:
            msg.is_read = True
            msg.save()
        serializer = MessageSerializer(msgs_list, many=True)
        return HttpResponse(json.dumps(serializer.data), content_type='application/json')

    except Exception:
        return {"error": "check the request, something went wrong!!!"}


@api_view(['POST', 'PUT'])
def create_message(request):
    """" create the message by the giving parameters """
    try:
        json_data = json.loads(request.body)
        new_msg = Message()
        new_msg.sender = json_data['sender']
        new_msg.reciever = json_data['reciever']
        new_msg.subject = json_data['subject']
        new_msg.message = json_data['message']
        new_msg.save()
        serializer = MessageSerializer(new_msg, many=False)
        return HttpResponse(json.dumps(serializer.data), content_type='application/json')

    except Exception:
        return {"error": "check the request, something went wrong!!!"}


@api_view(['DELETE'])
def delete_message(request):
    """" delete the message by the giving id """
    try:
        print('im start to deleting')
        json_data = json.loads(request.body)
        msgs_list = Message.objects.filter(reciever=json_data['email'], id=json_data['id'])
        msgs_list2 = Message.objects.filter(sender=json_data['email'], id=json_data['id'])
        if not msgs_list and not msgs_list2:
            return HttpResponse('There are no message with this id to delete')
        for msg in msgs_list:
            print('im deleting')
            msg.delete()

        for msg in msgs_list2:
            print('im deleting')
            msg.delete()

        return HttpResponse('message deleted successfully')
    except Exception:
        return {"error": "check the request, something went wrong!!!"}


