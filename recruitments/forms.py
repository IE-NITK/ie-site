from django import forms
from django.db import models as model
from recruitments import models
from SIG.models import SIGroup
from django.forms.widgets import CheckboxSelectMultiple
from captcha.fields import ReCaptchaField

#form to be used by candidates to submit resumes
class FillResumeForm(forms.ModelForm):
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name *"
        self.fields['roll_number'].label = "Roll Number * (eg. 16CO102)"
        self.fields['gender'].label = "Gender *"
        self.fields['phone_number'].label = "WhatsApp Number * (10 digits)"
        self.fields['email_id'].label = "Email ID *"
        self.fields['why_ie'].label = "Why are you looking to join a technical club and why specifically IE? *"
        self.fields['core_sig_choice'].label = "What Core SIG(s) would you like to be a part of? *"
        #self.fields['core_sig_choice'].widget = CheckboxSelectMultiple()
        # self.fields['core_sig_choice'].widget = forms.RadioSelect()
        # self.fields['core_sig_choice'].queryset = SIGroup.objects.exclude(core=False)
        self.fields['core_sig_choice_2'].label = "Any other Core SIG(s) you would like to be a part of, if any?"
        # self.fields['core_sig_choice_2'].widget = CheckboxSelectMultiple()
        # self.fields['core_sig_choice_2'].queryset = SIGroup.objects.exclude(core=False)
        self.fields['core_sig_projects'].label = "Have you done any work relevant to the SIGs you chose? Do you have any new project ideas?"
        #self.fields['core_sig_projects'].required = False
        self.fields['script_essay'].label = "Script essay"
        self.fields['script_essay'].required = False
        self.fields['robotics_essay'].label = "Robotics essay"
        self.fields['robotics_essay'].required = False
        # self.fields['aux_sig_choice'].label = "What Auxiliary SIG(s) would you like to be a part of?"
        # self.fields['aux_sig_choice'].widget = CheckboxSelectMultiple()
        # self.fields['aux_sig_choice'].queryset = SIGroup.objects.exclude(core=True)
        # self.fields['aux_sig_choice'].required = False
        # self.fields['aux_sig_interests'].label = "Do you have any ideas for new SIGs? Please explain."
        # self.fields['aux_sig_interests'].required = False
        self.fields['event_participation'].label = "Have you participated in any IE events last year? How was your experience? *"
        #self.fields['event_participation'].required = True
        self.fields['video'].label = "Are you interested in Video Editing, Poster Designing? If yes, then which software/tools do you use?"
        #self.fields['video'].required = False
        #self.fields['spark'].label = "Spark is a TEDx inspired talk event aimed to promote creative thinking and sharing ideas. Given an opportunity, what would you want to talk about on the Spark platform? *"
        self.fields['about_me'].label = "If you were a brand, what would be your motto? Convince us that you are valuable. *"
        #self.fields['next_tech'].label = "What technology do you think is the next big thing w.r.t your interest SIG(s)? *"
        #self.fields['witty_question'].label = "In a small room, you have a refrigerator. If you left the door of the fridge open, what would happen to the temperature in the room? Explain in layman terms. *"
        self.fields['picture'].label = "Tell us what thoughts come to mind when you see the picture below. *"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = models.Resume
        fields = [
            'name',
            'roll_number',
            'gender',
            'phone_number',
            'email_id',
			'why_ie',
			'core_sig_choice',
            'core_sig_choice_2',
            'core_sig_projects',
            'script_essay',
            'robotics_essay',
			# 'aux_sig_choice',
            #'aux_sig_interests',
			'event_participation',
			'video',
			#'spark',
            'about_me',
            #'next_tech',
            #'witty_question',
            'picture',
            'captcha',
        ]


class FillFreshersForm(forms.Form):

    name = model.CharField(max_length=20)
    branch = model.CharField(max_length=40)

    def clean(self):
        return self.cleaned_data

#form to be used by members to grade resumes
class EvaluateResumeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['score'].label = "Score *"
        self.fields['comments'].label = "Break-up of Score *"
        self.fields['informal_comments'].label = "Impression of the Candidate(compulsory)/Informal Comments/P.M.S. *"
        self.fields['qualified'].label = "Qualified *"
        self.fields['qualified'].required = False
        self.fields['sig_evaluators'].label = "Name of the evaluator and SIG (for PIs, enter name of the SIG the candidate qualifies for and the name of the person who took the SIG-specific interview. for GDs, just enter the name of the evaluator.) *"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = models.ResumeEvaluation
        fields = [
            'score',
            'informal_comments',
            'comments',
            'qualified',
            'sig_evaluators'
        ]
