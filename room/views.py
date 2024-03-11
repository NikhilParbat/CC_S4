from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .serializers import RoomSerializer, MessageSerializer
from .models import Room, Message

@api_view(['GET'])
def room_list(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    serializer = RoomSerializer(room)
    return Response(serializer.data)

@api_view(['GET'])
def message_list(request, room_slug):
    room = Room.objects.get(slug=room_slug)
    messages = Message.objects.filter(room=room)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def new_message(request, room_slug):
    room = Room.objects.get(slug=room_slug)
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(room=room, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def join_room(request):
    # Get the room slug from the request data
    slug = request.data.get('slug')

    # Retrieve the room object from the database
    try:
        room = Room.objects.get(slug=slug)
    except Room.DoesNotExist:
        raise NotFound("Room not found.")

    # Logic to join the room (you can implement this as needed)

    # Return a response indicating success
    serializer = RoomSerializer(room)
    return Response(serializer.data['name'])

@api_view(['POST'])
def room_create(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
    