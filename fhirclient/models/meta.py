#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Meta) on 2015-09-24.
#  2015, SMART Health IT.


from . import coding
from . import fhirdate
from . import fhirelement


class Meta(fhirelement.FHIRElement):
    """ Metadata about a resource.
    
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always be
    associated with version changes to the resource.
    """
    
    resource_name = "Meta"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.lastUpdated = None
        """ When the resource version last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profiles this resource claims to conform to.
        List of `str` items. """
        
        self.security = None
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.tag = None
        """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.versionId = None
        """ Version specific identifier.
        Type `str`. """
        
        super(Meta, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend([
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False),
            ("profile", "profile", str, True),
            ("security", "security", coding.Coding, True),
            ("tag", "tag", coding.Coding, True),
            ("versionId", "versionId", str, False),
        ])
        return js

