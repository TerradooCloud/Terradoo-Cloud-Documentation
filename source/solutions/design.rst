.. _design:

Design
######

Microservices Architecture
**************************

Pattern design: `The Twelve-Factor APP Design <https://12factor.net/>`_


`CNCF Overview Landscape <https://landscape.cncf.io/>`_


Considerations
**************

-  Design Solutions

    -  Define Proof of Concept ( Business Study Case )

      -  Define Business Requirements
      -  Define Billing 
      -  Define Business SLI 
      -  Define Business SLO
      -  Define Business SLA

    -  Design Technical Solutions

        -  Define Technical Requirements
        -  Define Technical KPI
        -  Design Infrastructure Architecture Solutions
        
          -  Design Integration Solutions
          -  Design Storage Solutions
          -  Design Network Solutions
          -  Design Deployment Solutions
          -  Design Reliable Scalable Solutions
          -  Design Security Solutions
          -  Design Monitoring Solutions
          -  Design Communications Solutions


General Workflow
****************

  - GitHub as VCS with Terraform templates

  - Terraform Cloud Operator for Multi Cloud Infrastrucure Layer

  - Provision Kubernetes Layer
  
  - Provision Helmv3 Layer

  - Provision custom charts from ArtifactHub for custom stack around Odoo Community