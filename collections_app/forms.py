from django import forms

from collections_app.models import Collection


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('name', 'is_private')


class AddToCollectionForm(forms.Form):
    collections = forms.ModelChoiceField(
        queryset=Collection.objects.none(),
        label="Выберите Коллекцию",
        widget=forms.Select()
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields["collections"].queryset = Collection.objects.filter(user=user)
            if not self.fields['collections'].queryset.exists():
                self.fields['collections'].widget = forms.HiddenInput()
        else:
            self.fields['collections'].widget = forms.HiddenInput()
