from django import forms


class TriangleForm(forms.Form):
    """A form for inputting triangle catheti lengths

    Attributes:
        cathetus_1 (forms.IntegerField): The input field for cathetus 1
        cathetus_2 (forms.IntegerField): The input field for cathetus 2
    """

    cathetus_1 = forms.IntegerField(
        label="Cathetus 1",
        widget=forms.NumberInput(attrs={"placeholder": "Enter the number"}),
        required=False,
    )

    cathetus_2 = forms.IntegerField(
        label="Cathetus 2",
        widget=forms.NumberInput(attrs={"placeholder": "Enter the number"}),
        required=False,
    )

    def clean_cathetus(self, field) -> int:
        """Clean and validate the given cathetus field

        Args:
            field(str): the name of the cathetus field to be cleaned

        Returns:
            cathetus(int): the cleaned value of the cathetus field

        Raises:
            forms.ValidationError: if the cathetus value is not within
                                   the valid range or if the field is empty
        """
        cathetus = self.cleaned_data.get(field)
        if cathetus:
            if cathetus < 1 or cathetus > 1000000000:
                raise forms.ValidationError(
                    f"{field.capitalize().replace('_', ' ')} must be between 1 and 1 000 000 000"
                )
        else:
            raise forms.ValidationError("This field is required.")
        return cathetus

    def clean_cathetus_1(self) -> int:
        """Clean and validate cathetus_1 field using the clean_cathetus method

        Returns:
            cathetus(int): the cleaned value of the cathetus_1 field
        """
        cathetus = self.clean_cathetus("cathetus_1")
        return cathetus

    def clean_cathetus_2(self) -> int:
        """Clean and validate cathetus_2 field using the clean_cathetus method

        Returns:
            cathetus(int): the cleaned value of the cathetus_2 field
        """
        cathetus = self.clean_cathetus("cathetus_2")
        return cathetus
