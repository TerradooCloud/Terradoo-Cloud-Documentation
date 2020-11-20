.. _design:

Design
######

Microservices Architecture
**************************

Patron design solution: `The Twelve-Factor APP Design <https://12factor.net/>`_


`CNCF Overview Landscape <https://landscape.cncf.io/>`_


Considerations
**************

-  Design Solution

    -  Define Proof of Concept ( Business Study Case )

      -  Define Business Requirements
      -  Define Billing 
      -  Define Business SLI 
      -  Define Business SLO
      -  Define Business SLA

    -  Design Technical Solution

        -  Define Technical Requirements
        -  Define Technical KPI
        -  Design Infrastructure Architecture Solution
        
          -  Design Integration Solution
          -  Design Storage Solution
          -  Design Network Solution
          -  Design Deployment Solution
          -  Design Reliable Scalable Solution
          -  Design Security Solution
          -  Design Monitoring Solution
          -  Design Communications Solution


General Workflow
****************

  - GitHub as VCS with Terraform templates

  - Terraform Cloud Operator for Multi Cloud Infrastrucure Layer

  - Provision Kubernetes Layer
  
  - Provision Helmv3 Layer

  - Provision custom charts from ArtifactHub for custom stack around Odoo Community