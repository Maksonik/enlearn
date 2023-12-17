# serializers.py
from rest_framework import serializers
from .models import Word, Description, Sound, Phrase, Form, Example


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['region', 'transcription', 'link', 'sound']


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ['phrase', 'translate']


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['part_of_speech', 'condition', 'value']


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['part_of_speech', 'general_meaning', 'deep_meaning', 'translate']


class ExampleSerializerWord(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['example', 'translate']


class WordSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True)
    sounds = SoundSerializer(many=True)
    phrases = PhraseSerializer(many=True)
    forms = FormSerializer(many=True)
    examples = ExampleSerializerWord(many=True, read_only=True)

    class Meta:
        model = Word
        fields = ['name', 'short_description', 'rank', 'descriptions', 'sounds', 'phrases', 'forms', 'examples']

    def create(self, validated_data):
        """
        Создание слова через API
        """
        descriptions_data = validated_data.pop('descriptions', [])
        sounds_data = validated_data.pop('sounds', [])
        phrases_data = validated_data.pop('phrases', [])
        forms_data = validated_data.pop('forms', [])

        word = Word.objects.create(**validated_data)

        for description_data in descriptions_data:
            word.descriptions.add(Description.objects.create(word=word, **description_data))

        for sound_data in sounds_data:
            word.sounds.add(Sound.objects.create(word=word, **sound_data))

        for phrase_data in phrases_data:
            word.phrases.add(Phrase.objects.create(word=word, **phrase_data))

        for form_data in forms_data:
            word.forms.add(Form.objects.create(word=word, **form_data))

        return word
    
    
class WordSerializerExample(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['name', 'short_description', 'rank']


class ExampleSerializer(serializers.ModelSerializer):
    words = WordSerializerExample(many=True, required=False)

    class Meta:
        model = Example
        fields = ['example', 'translate', 'words']

    def create(self, validated_data):
        example = Example.objects.create(**validated_data)

        for word in validated_data['example'].split(' '):
            word = word.strip(',/!&?."\\ ').lower()
            try:
                obj = Word.objects.get(name=word)
                example.words.add(obj)
            except Word.DoesNotExist:
                continue

        return example
