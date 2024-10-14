from rest_framework import serializers
from imdb_list.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"  #if i want all fields to show then write this 
        # fields = ['id','name','description']  #if i want to show some selected fields 
        # exclude = ['name']  #if i want dont show selected fields 

    def get_len_name(self,object):
        return len(object.name)
        
    def validate_name(self,value):
        if len(value) < 2:
            raise serializers.ValidationError('Name should be at least 2 characters long.')
        else:
            return value
        
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description should not be the same.')
        else:
            return data
        
class StreamPlatformSerializers(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name should be at least 2 characters long.')
    
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):  #here instance carried old or current values which i want updated
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    # field label validation
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name should be at least 2 characters long.')
    #     else:
    #         return value
        
    # object label validation
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name and description should not be the same.')
    #     else:
    #         return data