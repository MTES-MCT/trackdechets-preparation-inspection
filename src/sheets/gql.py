graphql_query_csv = """
  query WastesRegistryCsv(
    $registryType: WasteRegistryType!
    $sirets: [String!]!,
    $where: WasteRegistryWhere
  ) {
    wastesRegistryCsv(
      registryType: $registryType
      sirets: $sirets
      where: $where
    ) {
      token
      downloadLink
    }
  }
"""

graphql_query_xls = """
  query WastesRegistryXls(
    $registryType: WasteRegistryType!
    $sirets: [String!]!,
    $where: WasteRegistryWhere
  ) {
    wastesRegistryXls(
      registryType: $registryType
      sirets: $sirets
       where: $where
    ) {
      token
      downloadLink
    }
  }
"""
