#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport) on 2015-09-24.
#  2015, SMART Health IT.


from . import attachment
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period


class DiagnosticReport(domainresource.DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """
    
    resource_name = "DiagnosticReport"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ Service category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Name/Code for this diagnostic report.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.codedDiagnosis = None
        """ Codes for the conclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.conclusion = None
        """ Clinical Interpretation of test results.
        Type `str`. """
        
        self.effectiveDateTime = None
        """ Clinically Relevant time/time-period for report.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Clinically Relevant time/time-period for report.
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Health care event when test ordered.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Id for external references to this report.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.image = None
        """ Key images associated with this report.
        List of `DiagnosticReportImage` items (represented as `dict` in JSON). """
        
        self.imagingStudy = None
        """ Reference to full details of imaging associated with the diagnostic
        report.
        List of `FHIRReference` items referencing `ImagingStudy, ImagingObjectSelection` (represented as `dict` in JSON). """
        
        self.issued = None
        """ DateTime this version was released.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.performer = None
        """ Responsible Diagnostic Service.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.presentedForm = None
        """ Entire report as issued.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.request = None
        """ What was requested.
        List of `FHIRReference` items referencing `DiagnosticOrder, ProcedureRequest, ReferralRequest` (represented as `dict` in JSON). """
        
        self.result = None
        """ Observations - simple, or complex nested groups.
        List of `FHIRReference` items referencing `Observation` (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimens this report is based on.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | partial | final | corrected | appended | cancelled |
        entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ The subject of the report, usually, but not always, the patient.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """
        
        super(DiagnosticReport, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DiagnosticReport, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False),
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("codedDiagnosis", "codedDiagnosis", codeableconcept.CodeableConcept, True),
            ("conclusion", "conclusion", str, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("image", "image", DiagnosticReportImage, True),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, True),
            ("issued", "issued", fhirdate.FHIRDate, False),
            ("performer", "performer", fhirreference.FHIRReference, False),
            ("presentedForm", "presentedForm", attachment.Attachment, True),
            ("request", "request", fhirreference.FHIRReference, True),
            ("result", "result", fhirreference.FHIRReference, True),
            ("specimen", "specimen", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
        ])
        return js


class DiagnosticReportImage(fhirelement.FHIRElement):
    """ Key images associated with this report.
    
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    
    resource_name = "DiagnosticReportImage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comment = None
        """ Comment about the image (e.g. explanation).
        Type `str`. """
        
        self.link = None
        """ Reference to the image source.
        Type `FHIRReference` referencing `Media` (represented as `dict` in JSON). """
        
        super(DiagnosticReportImage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DiagnosticReportImage, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False),
            ("link", "link", fhirreference.FHIRReference, False),
        ])
        return js

