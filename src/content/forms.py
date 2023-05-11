from django import forms

USEFUL_CHOICES = (
    (0, "Inutile"),
    (1, "Peu utile"),
    (2, "Ne se prononce pas"),
    (3, "Utile"),
    (4, "Très utile"),
)
CLARITY_CHOICES = (
    (0, "Pas compréhensibles"),
    (1, "Peu compréhensibles"),
    (2, "Ne se prononce pas"),
    (3, "Compréhensibles"),
    (4, "Très compréhensibles"),
)
TIME_SAVED_CHOICES = (
    (0, "Perdre du temps"),
    (1, "Perdre un peu de temps"),
    (2, "Ne se prononce pas"),
    (3, "Gagner un peu de temps"),
    (4, "Gagner beaucoup de temps"),
)
TEXTAREA_CONFIG = {"cols": "40", "rows": "3"}


class FeedbackForm(forms.Form):
    was_useful = forms.ChoiceField(
        choices=USEFUL_CHOICES,
        label="Cette fiche vous a-t-elle été utile ?",
        widget=forms.RadioSelect,
    )
    did_save_time = forms.ChoiceField(
        choices=TIME_SAVED_CHOICES,
        label="Par rapport à votre inspection, vous a-t-elle permis de :",
        widget=forms.RadioSelect(),
    )
    time_saved = forms.CharField(
        required=False,
        label="Le cas échéant, quel temps pensez vous avoir gagné ?",
        help_text="Ex: 1,5h -  30 mn…",
    )
    was_clear = forms.ChoiceField(
        choices=CLARITY_CHOICES,
        label="Les informations présentées sont : ",
        widget=forms.RadioSelect,
    )
    was_clear_info = forms.CharField(
        required=False,
        label="Le cas échéant, quelles sont celles qui ne le sont pas ?",
        widget=forms.Textarea(attrs=TEXTAREA_CONFIG),
    )
    discrepencies = forms.CharField(
        required=False,
        label="Avez vous trouvé une anomalie entre la fiche et le terrain ?",
        help_text="(ex stock indiqué sur la fiche ne correspond pas à la réalité après visite)",
        widget=forms.Textarea(attrs=TEXTAREA_CONFIG),
    )
    discrepencies_siret = forms.CharField(
        required=False,
        label="Le cas échéant, quel siret était concerné par ces anomalies ?",
    )
    missing_infos = forms.CharField(
        required=False,
        label="Quelle sont les informations qui vous manquent pour améliorer la fiche et mieux vous aider ?",
        widget=forms.Textarea(attrs=TEXTAREA_CONFIG),
    )
    problems_found = forms.CharField(
        required=False,
        label="Est ce que la fiche d'inspection vous à permis de trouver des problèmes que vous n'auriez pas trouver sans ? Lesquels ?",
        widget=forms.Textarea(attrs=TEXTAREA_CONFIG),
    )
    infos = forms.CharField(
        required=False,
        label="Remarques complémentaires et suggestions",
        widget=forms.Textarea(attrs=TEXTAREA_CONFIG),
    )

    def to_content(self):
        if not self.is_valid():
            return ""
        content = []

        for field_name, field in self.fields.items():
            value = self.cleaned_data.get(field_name)
            if isinstance(field, forms.ChoiceField):
                try:
                    value = int(value)
                except ValueError:
                    pass
                verbose_value = dict(field.choices)[value]
            else:
                verbose_value = self.cleaned_data.get(field_name)
            content.append(f"{field.label} {verbose_value}")
        return "\n".join(content)
