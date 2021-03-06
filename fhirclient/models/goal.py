#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Goal) on 2015-09-24.
#  2015, SMART Health IT.


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity


class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.
    
    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    
    resource_name = "Goal"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.addresses = None
        """ Issues addressed by this goal.
        List of `FHIRReference` items referencing `Condition, Observation, MedicationStatement, NutritionOrder, ProcedureRequest, RiskAssessment` (represented as `dict` in JSON). """
        
        self.author = None
        """ Who's responsible for creating Goal?.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.category = None
        """ E.g. Treatment, dietary, behavioral, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ What's the desired outcome?.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this goal.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments about the goal.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ What was end result of goal?.
        List of `GoalOutcome` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ high | medium |low.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startCodeableConcept = None
        """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startDate = None
        """ When goal pursuit begins.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ proposed | planned | accepted | rejected | in-progress | achieved |
        sustaining | on-hold | cancelled.
        Type `str`. """
        
        self.statusDate = None
        """ When goal status took effect.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who this goal is intended for.
        Type `FHIRReference` referencing `Patient, Group, Organization` (represented as `dict` in JSON). """
        
        self.targetDate = None
        """ Reach goal on or before.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.targetQuantity = None
        """ Reach goal on or before.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """
        
        super(Goal, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("addresses", "addresses", fhirreference.FHIRReference, True),
            ("author", "author", fhirreference.FHIRReference, False),
            ("category", "category", codeableconcept.CodeableConcept, True),
            ("description", "description", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("note", "note", annotation.Annotation, True),
            ("outcome", "outcome", GoalOutcome, True),
            ("priority", "priority", codeableconcept.CodeableConcept, False),
            ("startCodeableConcept", "startCodeableConcept", codeableconcept.CodeableConcept, False),
            ("startDate", "startDate", fhirdate.FHIRDate, False),
            ("status", "status", str, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("targetDate", "targetDate", fhirdate.FHIRDate, False),
            ("targetQuantity", "targetQuantity", quantity.Quantity, False),
        ])
        return js


class GoalOutcome(fhirelement.FHIRElement):
    """ What was end result of goal?.
    
    Identifies the change (or lack of change) at the point where the goal was
    deepmed to be cancelled or achieved.
    """
    
    resource_name = "GoalOutcome"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.resultCodeableConcept = None
        """ Code or observation that resulted from goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.resultReference = None
        """ Code or observation that resulted from goal.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        super(GoalOutcome, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(GoalOutcome, self).elementProperties()
        js.extend([
            ("resultCodeableConcept", "resultCodeableConcept", codeableconcept.CodeableConcept, False),
            ("resultReference", "resultReference", fhirreference.FHIRReference, False),
        ])
        return js

