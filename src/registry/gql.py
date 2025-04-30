graphql_generate_registry_export = """
  mutation GenerateRegistryV2Export(
    $registryType: RegistryV2ExportType!
    $siret: String,
    $format: FormsRegisterExportFormat!
    $dateRange: DateFilter!
  ) {
    generateRegistryV2Export(
     registryType: $registryType, 
     format: $format, 
     siret: $siret, 
     dateRange: $dateRange
    ) {
      id
      status
    }
  }
"""

graphql_read_registry_export = """
query RegistryV2Export($id: ID!)
 
  {
  registryV2Export(id: $id)
  {
   
        id
        createdBy {id name}
        status
        format
  
  }
} 
"""


graphql_registry_V2_export_download_signed_url = """
query RegistryV2ExportDownloadSignedUrl($exportId: String!) {
  registryV2ExportDownloadSignedUrl(exportId: $exportId) {
    signedUrl
  }
}
"""
