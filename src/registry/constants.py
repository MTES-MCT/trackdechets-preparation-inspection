from django.db import models

REGISTRY_TYPE_ALL = "ALL"
REGISTRY_TYPE_INCOMING = "INCOMING"
REGISTRY_TYPE_OUTGOING = "OUTGOING"
REGISTRY_TYPE_TRANSPORTED = "TRANSPORTED"
REGISTRY_FORMAT_CSV = "csv"
REGISTRY_FORMAT_XLS = "xls"


class RegistryV2Format(models.TextChoices):
    CSV = "CSV", "Texte (.csv)"
    XLS = "XLS", "Excel (.xlsx)"


class RegistryV2ExportState(models.TextChoices):
    """State options for processing tasks."""

    PENDING = "PENDING", "En attente"
    STARTED = "STARTED", "En cours"
    SUCCESSFUL = "SUCCESSFUL", "Terminé"
    FAILED = "FAILED", "Erreur"
    CANCELED = "CANCELED", "Annulé"


class RegistryV2ExportType(models.TextChoices):
    """Export types for registry v2."""

    # Registre exhaustif.
    # Registre qui n'est pas réglementaire et qui est indépendant des autres registres. Il permet
    # d'exporter un nombre d'informations conséquent sur l'ensemble des bordereaux sur lesquels un
    # acteur a été visé à partir du moment où l'enlèvement a été signé. Dans cet export, les bordereaux
    # sont triés par date d'enlèvement du déchet.
    # ALL = "ALL", "Registre exhaustif"

    # Registre entrant.
    # Registre réglementaire, les déchets apparaissent à partir du moment où l'enlèvement
    # a été signé et sont triés par date de réception du déchet.
    # https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000043884574
    INCOMING = "INCOMING", "Registre entrant"

    # Registre de gestion.
    # Registre réglementaire, les déchets apparaissent à partir du moment où l'enlèvement
    # a été signé et sont triés par date d'enlèvement du déchet (la date d'acquisition ou
    # de début de gestion du déchet n'apparaissant pas sur les bordereaux de suivi de déchet,
    # il n'est pas possible de trier le registre suivant cette date).
    # https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000043884599
    MANAGED = "MANAGED", "Registre de gestion"

    # Registre sortant.
    # Registre réglementaire, les déchets apparaissent à partir du moment où l'enlèvement
    # a été signé et sont triés par date d'enlèvement du déchet.
    # https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000043884583
    OUTGOING = "OUTGOING", "Registre sortant"

    # Registre Sortie de statut de déchet.
    SSD = "SSD", "Registre Sortie de statut de déchet"

    # Registre de transport.
    # Registre réglementaire, les déchets apparaissent à partir du moment où l'enlèvement
    # a été signé et sont triés par date d'enlèvement du déchet.
    # https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000043884592
    TRANSPORTED = "TRANSPORTED", "Registre de transport"


class RegistryV2DeclarationType(models.TextChoices):
    """Types of declarations."""

    # Tous types
    ALL = "ALL", "Tous"

    # Bordereau
    BSD = "BSD", "Tracé (bordereaux)"

    # Registre
    REGISTRY = "REGISTRY", "Déclaré (registre national)"


class RegistryV2WasteCode(models.TextChoices):
    """European Waste Catalogue codes with descriptions."""

    WASTE_01_01_01 = "01 01 01", "01 01 01 - déchets provenant de l'extraction des minéraux métallifères"
    WASTE_01_01_02 = "01 01 02", "01 01 02 - déchets provenant de l'extraction des minéraux non métallifères"
    WASTE_01_03_04 = "01 03 04*", "01 03 04* - stériles acidogènes provenant de la transformation du sulfure"
    WASTE_01_03_05 = "01 03 05*", "01 03 05* - autres stériles contenant des substances dangereuses"
    WASTE_01_03_06 = "01 03 06", "01 03 06 - stériles autres que ceux visés aux rubriques 01 03 04 et 01 03 05"
    WASTE_01_03_07 = (
        "01 03 07*",
        "01 03 07* - autres déchets contenant des substances dangereuses provenant de la transformation physique et chimique des minéraux métallifères",
    )
    WASTE_01_03_08 = (
        "01 03 08",
        "01 03 08 - déchets de poussières et de poudres autres que ceux visés à la rubrique 01 03 07",
    )
    WASTE_01_03_09 = (
        "01 03 09",
        "01 03 09 - boues rouges issues de la production d'alumine autres que celles visées à la rubrique 01 03 10",
    )
    WASTE_01_03_10 = (
        "01 03 10*",
        "01 03 10* - boues rouges issues de la production d'alumine contenant des substances dangereuses, autres que les déchets visés à la rubrique 01 03 07",
    )
    WASTE_01_03_99 = "01 03 99", "01 03 99 - déchets non spécifiés ailleurs"
    WASTE_01_04_07 = (
        "01 04 07*",
        "01 04 07* - déchets contenant des substances dangereuses provenant de la transformation physique et chimique des minéraux non métallifères",
    )
    WASTE_01_04_08 = (
        "01 04 08",
        "01 04 08 - déchets de graviers et débris de pierres autres que ceux visés à la rubrique 01 04 07",
    )
    WASTE_01_04_09 = "01 04 09", "01 04 09 - déchets de sable et d'argile"
    WASTE_01_04_10 = (
        "01 04 10",
        "01 04 10 - déchets de poussières et de poudres autres que ceux visés à la rubrique 01 04 07",
    )
    WASTE_01_04_11 = (
        "01 04 11",
        "01 04 11 - déchets de la transformation de la potasse et des sels minéraux autres que ceux visés à la rubrique 01 04 07",
    )
    WASTE_01_04_12 = (
        "01 04 12",
        "01 04 12 - stériles et autres déchets provenant du lavage et du nettoyage des minéraux autres que ceux visés aux rubriques 01 04 07 et 01 04 11",
    )
    WASTE_01_04_13 = (
        "01 04 13",
        "01 04 13 - déchets provenant de la taille et du sciage des pierres autres que ceux visés à la rubrique 01 04 07",
    )
    WASTE_01_04_99 = "01 04 99", "01 04 99 - déchets non spécifiés ailleurs"
    WASTE_01_05_04 = "01 05 04", "01 05 04 - boues et autres déchets de forage à l'eau douce"
    WASTE_01_05_05 = "01 05 05*", "01 05 05* - boues et autres déchets de forage contenant des hydrocarbures"
    WASTE_01_05_06 = (
        "01 05 06*",
        "01 05 06* - boues de forage et autres déchets de forage contenant des substances dangereuses",
    )
    WASTE_01_05_07 = (
        "01 05 07",
        "01 05 07 - boues et autres déchets de forage contenant des sels de baryum, autres que ceux visés aux rubriques 01 05 05 et 01 05 06",
    )
    WASTE_01_05_08 = (
        "01 05 08",
        "01 05 08 - boues et autres déchets de forage contenant des chlorures, autres que ceux visés aux rubriques 01 05 05 et 01 05 06",
    )
    WASTE_01_05_99 = "01 05 99", "01 05 99 - déchets non spécifiés ailleurs"
    WASTE_02_01_01 = "02 01 01", "02 01 01 - boues provenant du lavage et du nettoyage"
    WASTE_02_01_02 = "02 01 02", "02 01 02 - déchets de tissus animaux"
    WASTE_02_01_03 = "02 01 03", "02 01 03 - déchets de tissus végétaux"
    WASTE_02_01_04 = "02 01 04", "02 01 04 - déchets de matières plastiques (à l'exclusion des emballages)"
    WASTE_02_01_06 = (
        "02 01 06",
        "02 01 06 - fèces, urine et fumier (y compris paille souillée), effluents, collectés séparément et traités hors site",
    )
    WASTE_02_01_07 = "02 01 07", "02 01 07 - déchets provenant de la sylviculture"
    WASTE_02_01_08 = "02 01 08*", "02 01 08* - déchets agrochimiques contenant des substances dangereuses"
    WASTE_02_01_09 = "02 01 09", "02 01 09 - déchets agrochimiques autres que ceux visés à la rubrique 02 01 08"
    WASTE_02_01_10 = "02 01 10", "02 01 10 - déchets métalliques"
    WASTE_02_01_99 = "02 01 99", "02 01 99 - déchets non spécifiés ailleurs"
    WASTE_02_02_01 = "02 02 01", "02 02 01 - boues provenant du lavage et du nettoyage"
    WASTE_02_02_02 = "02 02 02", "02 02 02 - déchets de tissus animaux"
    WASTE_02_02_03 = "02 02 03", "02 02 03 - matières impropres à la consommation ou à la transformation"
    WASTE_02_02_04 = "02 02 04", "02 02 04 - boues provenant du traitement in situ des effluents"
    WASTE_02_02_99 = "02 02 99", "02 02 99 - déchets non spécifiés ailleurs"
    WASTE_02_03_01 = (
        "02 03 01",
        "02 03 01 - boues provenant du lavage, du nettoyage, de l'épluchage, de la centrifugation et de la séparation",
    )
    WASTE_02_03_02 = "02 03 02", "02 03 02 - déchets d'agents de conservation"
    WASTE_02_03_03 = "02 03 03", "02 03 03 - déchets de l'extraction aux solvants"
    WASTE_02_03_04 = "02 03 04", "02 03 04 - matières impropres à la consommation ou à la transformation"
    WASTE_02_03_05 = "02 03 05", "02 03 05 - boues provenant du traitement in situ des effluents"
    WASTE_02_03_99 = "02 03 99", "02 03 99 - déchets non spécifiés ailleurs"
    WASTE_02_04_01 = "02 04 01", "02 04 01 - terre provenant du lavage et du nettoyage des betteraves"
    WASTE_02_04_02 = "02 04 02", "02 04 02 - carbonate de calcium déclassé"
    WASTE_02_04_03 = "02 04 03", "02 04 03 - boues provenant du traitement in situ des effluents"
    WASTE_02_04_99 = "02 04 99", "02 04 99 - déchets non spécifiés ailleurs"
    WASTE_02_05_01 = "02 05 01", "02 05 01 - matières impropres à la consommation ou à la transformation"
    WASTE_02_05_02 = "02 05 02", "02 05 02 - boues provenant du traitement in situ des effluents"
    WASTE_02_05_99 = "02 05 99", "02 05 99 - déchets non spécifiés ailleurs"
    WASTE_02_06_01 = "02 06 01", "02 06 01 - matières impropres à la consommation ou à la transformation"
    WASTE_02_06_02 = "02 06 02", "02 06 02 - déchets d'agents de conservation"
    WASTE_02_06_03 = "02 06 03", "02 06 03 - boues provenant du traitement in situ des effluents"
    WASTE_02_06_99 = "02 06 99", "02 06 99 - déchets non spécifiés ailleurs"
    WASTE_02_07_01 = (
        "02 07 01",
        "02 07 01 - déchets provenant du lavage, du nettoyage et de la réduction mécanique des matières premières",
    )
    WASTE_02_07_02 = "02 07 02", "02 07 02 - déchets de la distillation de l'alcool"
    WASTE_02_07_03 = "02 07 03", "02 07 03 - déchets de traitements chimiques"
    WASTE_02_07_04 = "02 07 04", "02 07 04 - matières impropres à la consommation ou à la transformation"
    WASTE_02_07_05 = "02 07 05", "02 07 05 - boues provenant du traitement in situ des effluents"
    WASTE_02_07_99 = "02 07 99", "02 07 99 - déchets non spécifiés ailleurs"
    WASTE_03_01_01 = "03 01 01", "03 01 01 - déchets d'écorce et de liège"
    WASTE_03_01_04 = (
        "03 01 04*",
        "03 01 04* - sciure de bois, copeaux, chutes, bois, panneaux de particules et placages contenant des substances dangereuses",
    )
    WASTE_03_01_05 = (
        "03 01 05",
        "03 01 05 - sciure de bois, copeaux, chutes, bois, panneaux de particules et placages autres que ceux visés à la rubrique 03 01 04",
    )
    WASTE_03_01_99 = "03 01 99", "03 01 99 - déchets non spécifiés ailleurs"
    WASTE_03_02_01 = "03 02 01*", "03 02 01* - composés organiques non halogénés de protection du bois"
    WASTE_03_02_02 = "03 02 02*", "03 02 02* - composés organochlorés de protection du bois"
    WASTE_03_02_03 = "03 02 03*", "03 02 03* - composés organométalliques de protection du bois"
    WASTE_03_02_04 = "03 02 04*", "03 02 04* - composés inorganiques de protection du bois"
    WASTE_03_02_05 = (
        "03 02 05*",
        "03 02 05* - autres produits de protection du bois contenant des substances dangereuses",
    )
    WASTE_03_02_99 = "03 02 99", "03 02 99 - produits de protection du bois non spécifiés ailleurs"
    WASTE_03_03_01 = "03 03 01", "03 03 01 - déchets d'écorce et de bois"
    WASTE_03_03_02 = "03 03 02", "03 03 02 - liqueurs vertes (provenant de la récupération de liqueur de cuisson)"
    WASTE_03_03_05 = "03 03 05", "03 03 05 - boues de désencrage provenant du recyclage du papier"
    WASTE_03_03_07 = (
        "03 03 07",
        "03 03 07 - refus séparés mécaniquement provenant du broyage de déchets de papier et de carton",
    )
    WASTE_03_03_08 = "03 03 08", "03 03 08 - déchets provenant du tri de papier et de carton destinés au recyclage"
    WASTE_03_03_09 = "03 03 09", "03 03 09 - déchets de boues résiduaires de chaux"
    WASTE_03_03_10 = (
        "03 03 10",
        "03 03 10 - refus fibreux, boues de fibres, de charge et de couchage provenant d'une séparation mécanique",
    )
    WASTE_03_03_11 = (
        "03 03 11",
        "03 03 11 - boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 03 03 10",
    )
    WASTE_03_03_99 = "03 03 99", "03 03 99 - déchets non spécifiés ailleurs"
    WASTE_04_01_01 = "04 01 01", "04 01 01 - déchets d'écharnage et refentes"
    WASTE_04_01_02 = "04 01 02", "04 01 02 - résidus de pelanage"
    WASTE_04_01_03 = "04 01 03*", "04 01 03* - déchets de dégraissage contenant des solvants sans phase liquide"
    WASTE_04_01_04 = "04 01 04", "04 01 04 - liqueur de tannage contenant du chrome"
    WASTE_04_01_05 = "04 01 05", "04 01 05 - liqueur de tannage sans chrome"
    WASTE_04_01_06 = (
        "04 01 06",
        "04 01 06 - boues, notamment provenant du traitement in situ des effluents, contenant du chrome",
    )
    WASTE_04_01_07 = (
        "04 01 07",
        "04 01 07 - boues, notamment provenant du traitement in situ des effluents, sans chrome",
    )
    WASTE_04_01_08 = (
        "04 01 08",
        "04 01 08 - déchets de cuir tanné (refentes sur bleu, dérayures, échantillonnages, poussières de ponçage), contenant du chrome",
    )
    WASTE_04_01_09 = "04 01 09", "04 01 09 - déchets provenant de l'habillage et des finitions"
    WASTE_04_01_99 = "04 01 99", "04 01 99 - déchets non spécifiés ailleurs"
    WASTE_04_02_09 = "04 02 09", "04 02 09 - matériaux composites (textile imprégné, élastomère, plastomère)"
    WASTE_04_02_10 = (
        "04 02 10",
        "04 02 10 - matières organiques issues de produits naturels (par exemple graisse, cire)",
    )
    WASTE_04_02_14 = "04 02 14*", "04 02 14* - déchets provenant des finitions contenant des solvants organiques"
    WASTE_04_02_15 = (
        "04 02 15",
        "04 02 15 - déchets provenant des finitions autres que ceux visés à la rubrique 04 02 14",
    )
    WASTE_04_02_16 = "04 02 16*", "04 02 16* - teintures et pigments contenant des substances dangereuses"
    WASTE_04_02_17 = "04 02 17", "04 02 17 - teintures et pigments autres que ceux visés à la rubrique 04 02 16"
    WASTE_04_02_19 = (
        "04 02 19*",
        "04 02 19* - boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_04_02_20 = (
        "04 02 20",
        "04 02 20 - boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 04 02 19",
    )
    WASTE_04_02_21 = "04 02 21", "04 02 21 - fibres textiles non ouvrées"
    WASTE_04_02_22 = "04 02 22", "04 02 22 - fibres textiles ouvrées"
    WASTE_04_02_99 = "04 02 99", "04 02 99 - déchets non spécifiés ailleurs"
    WASTE_05_01_02 = "05 01 02*", "05 01 02* - boues de dessalage"
    WASTE_05_01_03 = "05 01 03*", "05 01 03* - boues de fond de cuves"
    WASTE_05_01_04 = "05 01 04*", "05 01 04* - boues d'alkyles acides"
    WASTE_05_01_05 = "05 01 05*", "05 01 05* - hydrocarbures accidentellement répandus"
    WASTE_05_01_06 = (
        "05 01 06*",
        "05 01 06* - boues contenant des hydrocarbures provenant des opérations de maintenance de l'installation ou des équipements",
    )
    WASTE_05_01_07 = "05 01 07*", "05 01 07* - goudrons acides"
    WASTE_05_01_08 = "05 01 08*", "05 01 08* - autres goudrons"
    WASTE_05_01_09 = (
        "05 01 09*",
        "05 01 09* - boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_05_01_10 = (
        "05 01 10",
        "05 01 10 - boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 05 01 09",
    )
    WASTE_05_01_11 = "05 01 11*", "05 01 11* - déchets provenant du nettoyage d'hydrocarbures avec des bases"
    WASTE_05_01_12 = "05 01 12*", "05 01 12* - hydrocarbures contenant des acides"
    WASTE_05_01_13 = "05 01 13", "05 01 13 - boues du traitement de l'eau d'alimentation des chaudières"
    WASTE_05_01_14 = "05 01 14", "05 01 14 - déchets provenant des colonnes de refroidissement"
    WASTE_05_01_15 = "05 01 15*", "05 01 15* - argiles de filtration usées"
    WASTE_05_01_16 = "05 01 16", "05 01 16 - déchets contenant du soufre provenant de la désulfuration du pétrole"
    WASTE_05_01_17 = "05 01 17", "05 01 17 - mélanges bitumineux"
    WASTE_05_01_99 = "05 01 99", "05 01 99 - déchets non spécifiés ailleurs"
    WASTE_05_06_01 = "05 06 01*", "05 06 01* - goudrons acides"
    WASTE_05_06_03 = "05 06 03*", "05 06 03* - autres goudrons"
    WASTE_05_06_04 = "05 06 04", "05 06 04 - déchets provenant des colonnes de refroidissement"
    WASTE_05_06_99 = "05 06 99", "05 06 99 - déchets non spécifiés ailleurs"
    WASTE_05_07_01 = "05 07 01*", "05 07 01* - déchets contenant du mercure"
    WASTE_05_07_02 = "05 07 02", "05 07 02 - déchets contenant du soufre"
    WASTE_05_07_99 = "05 07 99", "05 07 99 - déchets non spécifiés ailleurs"
    WASTE_06_01_01 = "06 01 01*", "06 01 01* - acide sulfurique et acide sulfureux"
    WASTE_06_01_02 = "06 01 02*", "06 01 02* - acide chlorhydrique"
    WASTE_06_01_03 = "06 01 03*", "06 01 03* - acide fluorhydrique"
    WASTE_06_01_04 = "06 01 04*", "06 01 04* - acide phosphorique et acide phosphoreux"
    WASTE_06_01_05 = "06 01 05*", "06 01 05* - acide nitrique et acide nitreux"
    WASTE_06_01_06 = "06 01 06*", "06 01 06* - autres acides"
    WASTE_06_01_99 = "06 01 99", "06 01 99 - déchets non spécifiés ailleurs"
    WASTE_06_02_01 = "06 02 01*", "06 02 01* - hydroxyde de calcium"
    WASTE_06_02_03 = "06 02 03*", "06 02 03* - hydroxyde d'ammonium"
    WASTE_06_02_04 = "06 02 04*", "06 02 04* - hydroxyde de sodium et hydroxyde de potassium"
    WASTE_06_02_05 = "06 02 05*", "06 02 05* - autres bases"
    WASTE_06_02_99 = "06 02 99", "06 02 99 - déchets non spécifiés ailleurs"
    WASTE_06_03_11 = "06 03 11*", "06 03 11* - sels et solutions contenant des cyanures"
    WASTE_06_03_13 = "06 03 13*", "06 03 13* - sels et solutions contenant des métaux lourds"
    WASTE_06_03_14 = (
        "06 03 14",
        "06 03 14 - sels solides et solutions autres que ceux visés aux rubriques 06 03 11 et 06 03 13",
    )
    WASTE_06_03_15 = "06 03 15*", "06 03 15* - oxydes métalliques contenant des métaux lourds"
    WASTE_06_03_16 = "06 03 16", "06 03 16 - oxydes métalliques autres que ceux visés à la rubrique 06 03 15"
    WASTE_06_03_99 = "06 03 99", "06 03 99 - déchets non spécifiés ailleurs"
    WASTE_06_04_03 = "06 04 03*", "06 04 03* - déchets contenant de l'arsenic"
    WASTE_06_04_04 = "06 04 04*", "06 04 04* - déchets contenant du mercure"
    WASTE_06_04_05 = "06 04 05*", "06 04 05* - déchets contenant d'autres métaux lourds"
    WASTE_06_04_99 = "06 04 99", "06 04 99 - déchets non spécifiés ailleurs"
    WASTE_06_05_02 = (
        "06 05 02*",
        "06 05 02* - boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_06_05_03 = (
        "06 05 03",
        "06 05 03 - boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 06 05 02",
    )
    WASTE_06_06_02 = "06 06 02*", "06 06 02* - déchets contenant des sulfures dangereux"
    WASTE_06_06_03 = (
        "06 06 03",
        "06 06 03 - déchets contenant des sulfures autres que ceux visés à la rubrique 06 06 02",
    )
    WASTE_06_06_99 = "06 06 99", "06 06 99 - déchets non spécifiés ailleurs"
    WASTE_06_07_01 = "06 07 01*", "06 07 01* - déchets contenant de l'amiante provenant de l'électrolyse"
    WASTE_06_07_02 = "06 07 02*", "06 07 02* - déchets de charbon actif utilisé pour la production du chlore"
    WASTE_06_07_03 = "06 07 03*", "06 07 03* - boues de sulfate de baryum contenant du mercure"
    WASTE_06_07_04 = "06 07 04*", "06 07 04* - solutions et acides, par exemple acide de contact"
    WASTE_06_07_99 = "06 07 99", "06 07 99 - déchets non spécifiés ailleurs"
    WASTE_06_08_02 = "06 08 02*", "06 08 02* - déchets contenant des chlorosilanes dangereux"
    WASTE_06_08_99 = "06 08 99", "06 08 99 - déchets non spécifiés ailleurs"
    WASTE_06_09_02 = "06 09 02", "06 09 02 - scories phosphoriques"
    WASTE_06_09_03 = (
        "06 09 03*",
        "06 09 03* - déchets de réactions basées sur le calcium contenant des substances dangereuses ou contaminées par de telles substances",
    )
    WASTE_06_09_04 = (
        "06 09 04",
        "06 09 04 - déchets de réactions basées sur le calcium autres que ceux visés à la rubrique 06 09 03",
    )
    WASTE_06_09_99 = "06 09 99", "06 09 99 - déchets non spécifiés ailleurs"
    WASTE_06_10_02 = "06 10 02*", "06 10 02* - déchets contenant des substances dangereuses"
    WASTE_06_10_99 = "06 10 99", "06 10 99 - déchets non spécifiés ailleurs"
    WASTE_06_11_01 = (
        "06 11 01",
        "06 11 01 - déchets de réactions basées sur le calcium provenant de la production de dioxyde de titane",
    )
    WASTE_06_11_99 = "06 11 99", "06 11 99 - déchets non spécifiés ailleurs"
    WASTE_06_13_01 = (
        "06 13 01*",
        "06 13 01* - produits phytosanitaires inorganiques, agents de protection du bois et autres biocides",
    )
    WASTE_06_13_02 = "06 13 02*", "06 13 02* - charbon actif usé (sauf rubrique 06 07 02)"
    WASTE_06_13_03 = "06 13 03", "06 13 03 - noir de carbone"
    WASTE_06_13_04 = "06 13 04*", "06 13 04* - déchets provenant de la transformation de l'amiante"
    WASTE_06_13_05 = "06 13 05*", "06 13 05* - suies"
    WASTE_06_13_99 = "06 13 99", "06 13 99 - déchets non spécifiés ailleurs"
    WASTE_07_01_01 = "07 01 01*", "07 01 01* - eaux de lavage et liqueurs mères aqueuses"
    WASTE_07_01_03 = "07 01 03*", "07 01 03* - solvants, liquides de lavage et liqueurs mères organiques halogénés"
    WASTE_07_01_04 = "07 01 04*", "07 01 04* - autres solvants, liquides de lavage et liqueurs mères organiques"
    WASTE_07_01_07 = "07 01 07*", "07 01 07* - résidus de réaction et résidus de distillation halogénés"
    WASTE_07_01_08 = "07 01 08*", "07 01 08* - autres résidus de réaction et résidus de distillation"
    WASTE_07_01_09 = "07 01 09*", "07 01 09* - gâteaux de filtration et absorbants usés halogénés"
    WASTE_07_01_10 = "07 01 10*", "07 01 10* - autres gâteaux de filtration et absorbants usés"
    WASTE_07_01_11 = (
        "07 01 11*",
        "07 01 11* - boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_07_01_12 = (
        "07 01 12",
        "07 01 12 - boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 07 01 11",
    )


class RegistryV2WasteCode_(models.TextChoices):
    """European Waste Catalogue codes with descriptions."""

    WASTE_01_01_01 = "01 01 01", "déchets provenant de l'extraction des minéraux métallifères"
    WASTE_01_01_02 = "01 01 02", "déchets provenant de l'extraction des minéraux non métallifères"
    WASTE_01_03_04 = "01 03 04*", "stériles acidogènes provenant de la transformation du sulfure"
    WASTE_01_03_05 = "01 03 05*", "autres stériles contenant des substances dangereuses"
    WASTE_01_03_06 = "01 03 06", "stériles autres que ceux visés aux rubriques 01 03 04 et 01 03 05"
    WASTE_01_03_07 = (
        "01 03 07*",
        "autres déchets contenant des substances dangereuses provenant de la transformation physique et chimique des minéraux métallifères",
    )
    WASTE_01_03_08 = "01 03 08", "déchets de poussières et de poudres autres que ceux visés à la rubrique 01 03 07"
    WASTE_01_03_09 = (
        "01 03 09",
        "boues rouges issues de la production d'alumine autres que celles visées à la rubrique 01 03 10",
    )
    WASTE_01_03_10 = (
        "01 03 10*",
        "boues rouges issues de la production d'alumine contenant des substances dangereuses, autres que les déchets visés à la rubrique 01 03 07",
    )
    WASTE_01_03_99 = "01 03 99", "déchets non spécifiés ailleurs"
    WASTE_01_04_07 = (
        "01 04 07*",
        "déchets contenant des substances dangereuses provenant de la transformation physique et chimique des minéraux non métallifères",
    )
    WASTE_01_04_08 = (
        "01 04 08",
        "déchets de graviers et débris de pierres autres que ceux visés à la rubrique 01 04 07",
    )
    WASTE_01_04_09 = "01 04 09", "déchets de sable et d'argile"
    WASTE_01_04_10 = "01 04 10", "déchets de poussières et de poudres autres que ceux visés à la rubrique 01 04 07"
    WASTE_01_04_11 = (
        "01 04 11",
        "déchets de la transformation de la potasse et des sels minéraux autres que ceux visés à la rubrique 01 04 07",
    )
    WASTE_01_04_12 = (
        "01 04 12",
        "stériles et autres déchets provenant du lavage et du nettoyage des minéraux autres que ceux visés aux rubriques 01 04 07 et 01 04 11",
    )
    WASTE_01_04_13 = (
        "01 04 13",
        "déchets provenant de la taille et du sciage des pierres autres que ceux visés à la rubrique 01 04 07",
    )
    WASTE_01_04_99 = "01 04 99", "déchets non spécifiés ailleurs"
    WASTE_01_05_04 = "01 05 04", "boues et autres déchets de forage à l'eau douce"
    WASTE_01_05_05 = "01 05 05*", "boues et autres déchets de forage contenant des hydrocarbures"
    WASTE_01_05_06 = "01 05 06*", "boues de forage et autres déchets de forage contenant des substances dangereuses"
    WASTE_01_05_07 = (
        "01 05 07",
        "boues et autres déchets de forage contenant des sels de baryum, autres que ceux visés aux rubriques 01 05 05 et 01 05 06",
    )
    WASTE_01_05_08 = (
        "01 05 08",
        "boues et autres déchets de forage contenant des chlorures, autres que ceux visés aux rubriques 01 05 05 et 01 05 06",
    )
    WASTE_01_05_99 = "01 05 99", "déchets non spécifiés ailleurs"
    WASTE_02_01_01 = "02 01 01", "boues provenant du lavage et du nettoyage"
    WASTE_02_01_02 = "02 01 02", "déchets de tissus animaux"
    WASTE_02_01_03 = "02 01 03", "déchets de tissus végétaux"
    WASTE_02_01_04 = "02 01 04", "déchets de matières plastiques (à l'exclusion des emballages)"
    WASTE_02_01_06 = (
        "02 01 06",
        "fèces, urine et fumier (y compris paille souillée), effluents, collectés séparément et traités hors site",
    )
    WASTE_02_01_07 = "02 01 07", "déchets provenant de la sylviculture"
    WASTE_02_01_08 = "02 01 08*", "déchets agrochimiques contenant des substances dangereuses"
    WASTE_02_01_09 = "02 01 09", "déchets agrochimiques autres que ceux visés à la rubrique 02 01 08"
    WASTE_02_01_10 = "02 01 10", "déchets métalliques"
    WASTE_02_01_99 = "02 01 99", "déchets non spécifiés ailleurs"
    WASTE_02_02_01 = "02 02 01", "boues provenant du lavage et du nettoyage"
    WASTE_02_02_02 = "02 02 02", "déchets de tissus animaux"
    WASTE_02_02_03 = "02 02 03", "matières impropres à la consommation ou à la transformation"
    WASTE_02_02_04 = "02 02 04", "boues provenant du traitement in situ des effluents"
    WASTE_02_02_99 = "02 02 99", "déchets non spécifiés ailleurs"
    WASTE_02_03_01 = (
        "02 03 01",
        "boues provenant du lavage, du nettoyage, de l'épluchage, de la centrifugation et de la séparation",
    )
    WASTE_02_03_02 = "02 03 02", "déchets d'agents de conservation"
    WASTE_02_03_03 = "02 03 03", "déchets de l'extraction aux solvants"
    WASTE_02_03_04 = "02 03 04", "matières impropres à la consommation ou à la transformation"
    WASTE_02_03_05 = "02 03 05", "boues provenant du traitement in situ des effluents"
    WASTE_02_03_99 = "02 03 99", "déchets non spécifiés ailleurs"
    WASTE_02_04_01 = "02 04 01", "terre provenant du lavage et du nettoyage des betteraves"
    WASTE_02_04_02 = "02 04 02", "carbonate de calcium déclassé"
    WASTE_02_04_03 = "02 04 03", "boues provenant du traitement in situ des effluents"
    WASTE_02_04_99 = "02 04 99", "déchets non spécifiés ailleurs"
    WASTE_02_05_01 = "02 05 01", "matières impropres à la consommation ou à la transformation"
    WASTE_02_05_02 = "02 05 02", "boues provenant du traitement in situ des effluents"
    WASTE_02_05_99 = "02 05 99", "déchets non spécifiés ailleurs"
    WASTE_02_06_01 = "02 06 01", "matières impropres à la consommation ou à la transformation"
    WASTE_02_06_02 = "02 06 02", "déchets d'agents de conservation"
    WASTE_02_06_03 = "02 06 03", "boues provenant du traitement in situ des effluents"
    WASTE_02_06_99 = "02 06 99", "déchets non spécifiés ailleurs"
    WASTE_02_07_01 = (
        "02 07 01",
        "déchets provenant du lavage, du nettoyage et de la réduction mécanique des matières premières",
    )
    WASTE_02_07_02 = "02 07 02", "déchets de la distillation de l'alcool"
    WASTE_02_07_03 = "02 07 03", "déchets de traitements chimiques"
    WASTE_02_07_04 = "02 07 04", "matières impropres à la consommation ou à la transformation"
    WASTE_02_07_05 = "02 07 05", "boues provenant du traitement in situ des effluents"
    WASTE_02_07_99 = "02 07 99", "déchets non spécifiés ailleurs"
    WASTE_03_01_01 = "03 01 01", "déchets d'écorce et de liège"
    WASTE_03_01_04 = (
        "03 01 04*",
        "sciure de bois, copeaux, chutes, bois, panneaux de particules et placages contenant des substances dangereuses",
    )
    WASTE_03_01_05 = (
        "03 01 05",
        "sciure de bois, copeaux, chutes, bois, panneaux de particules et placages autres que ceux visés à la rubrique 03 01 04",
    )
    WASTE_03_01_99 = "03 01 99", "déchets non spécifiés ailleurs"
    WASTE_03_02_01 = "03 02 01*", "composés organiques non halogénés de protection du bois"
    WASTE_03_02_02 = "03 02 02*", "composés organochlorés de protection du bois"
    WASTE_03_02_03 = "03 02 03*", "composés organométalliques de protection du bois"
    WASTE_03_02_04 = "03 02 04*", "composés inorganiques de protection du bois"
    WASTE_03_02_05 = "03 02 05*", "autres produits de protection du bois contenant des substances dangereuses"
    WASTE_03_02_99 = "03 02 99", "produits de protection du bois non spécifiés ailleurs"
    WASTE_03_03_01 = "03 03 01", "déchets d'écorce et de bois"
    WASTE_03_03_02 = "03 03 02", "liqueurs vertes (provenant de la récupération de liqueur de cuisson)"
    WASTE_03_03_05 = "03 03 05", "boues de désencrage provenant du recyclage du papier"
    WASTE_03_03_07 = "03 03 07", "refus séparés mécaniquement provenant du broyage de déchets de papier et de carton"
    WASTE_03_03_08 = "03 03 08", "déchets provenant du tri de papier et de carton destinés au recyclage"
    WASTE_03_03_09 = "03 03 09", "déchets de boues résiduaires de chaux"
    WASTE_03_03_10 = (
        "03 03 10",
        "refus fibreux, boues de fibres, de charge et de couchage provenant d'une séparation mécanique",
    )
    WASTE_03_03_11 = (
        "03 03 11",
        "boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 03 03 10",
    )
    WASTE_03_03_99 = "03 03 99", "déchets non spécifiés ailleurs"
    WASTE_04_01_01 = "04 01 01", "déchets d'écharnage et refentes"
    WASTE_04_01_02 = "04 01 02", "résidus de pelanage"
    WASTE_04_01_03 = "04 01 03*", "déchets de dégraissage contenant des solvants sans phase liquide"
    WASTE_04_01_04 = "04 01 04", "liqueur de tannage contenant du chrome"
    WASTE_04_01_05 = "04 01 05", "liqueur de tannage sans chrome"
    WASTE_04_01_06 = "04 01 06", "boues, notamment provenant du traitement in situ des effluents, contenant du chrome"
    WASTE_04_01_07 = "04 01 07", "boues, notamment provenant du traitement in situ des effluents, sans chrome"
    WASTE_04_01_08 = (
        "04 01 08",
        "déchets de cuir tanné (refentes sur bleu, dérayures, échantillonnages, poussières de ponçage), contenant du chrome",
    )
    WASTE_04_01_09 = "04 01 09", "déchets provenant de l'habillage et des finitions"
    WASTE_04_01_99 = "04 01 99", "déchets non spécifiés ailleurs"
    WASTE_04_02_09 = "04 02 09", "matériaux composites (textile imprégné, élastomère, plastomère)"
    WASTE_04_02_10 = "04 02 10", "matières organiques issues de produits naturels (par exemple graisse, cire)"
    WASTE_04_02_14 = "04 02 14*", "déchets provenant des finitions contenant des solvants organiques"
    WASTE_04_02_15 = "04 02 15", "déchets provenant des finitions autres que ceux visés à la rubrique 04 02 14"
    WASTE_04_02_16 = "04 02 16*", "teintures et pigments contenant des substances dangereuses"
    WASTE_04_02_17 = "04 02 17", "teintures et pigments autres que ceux visés à la rubrique 04 02 16"
    WASTE_04_02_19 = (
        "04 02 19*",
        "boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_04_02_20 = (
        "04 02 20",
        "boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 04 02 19",
    )
    WASTE_04_02_21 = "04 02 21", "fibres textiles non ouvrées"
    WASTE_04_02_22 = "04 02 22", "fibres textiles ouvrées"
    WASTE_04_02_99 = "04 02 99", "déchets non spécifiés ailleurs"
    WASTE_05_01_02 = "05 01 02*", "boues de dessalage"
    WASTE_05_01_03 = "05 01 03*", "boues de fond de cuves"
    WASTE_05_01_04 = "05 01 04*", "boues d'alkyles acides"
    WASTE_05_01_05 = "05 01 05*", "hydrocarbures accidentellement répandus"
    WASTE_05_01_06 = (
        "05 01 06*",
        "boues contenant des hydrocarbures provenant des opérations de maintenance de l'installation ou des équipements",
    )
    WASTE_05_01_07 = "05 01 07*", "goudrons acides"
    WASTE_05_01_08 = "05 01 08*", "autres goudrons"
    WASTE_05_01_09 = (
        "05 01 09*",
        "boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_05_01_10 = (
        "05 01 10",
        "boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 05 01 09",
    )
    WASTE_05_01_11 = "05 01 11*", "déchets provenant du nettoyage d'hydrocarbures avec des bases"
    WASTE_05_01_12 = "05 01 12*", "hydrocarbures contenant des acides"
    WASTE_05_01_13 = "05 01 13", "boues du traitement de l'eau d'alimentation des chaudières"
    WASTE_05_01_14 = "05 01 14", "déchets provenant des colonnes de refroidissement"
    WASTE_05_01_15 = "05 01 15*", "argiles de filtration usées"
    WASTE_05_01_16 = "05 01 16", "déchets contenant du soufre provenant de la désulfuration du pétrole"
    WASTE_05_01_17 = "05 01 17", "mélanges bitumineux"
    WASTE_05_01_99 = "05 01 99", "déchets non spécifiés ailleurs"
    WASTE_05_06_01 = "05 06 01*", "goudrons acides"
    WASTE_05_06_03 = "05 06 03*", "autres goudrons"
    WASTE_05_06_04 = "05 06 04", "déchets provenant des colonnes de refroidissement"
    WASTE_05_06_99 = "05 06 99", "déchets non spécifiés ailleurs"
    WASTE_05_07_01 = "05 07 01*", "déchets contenant du mercure"
    WASTE_05_07_02 = "05 07 02", "déchets contenant du soufre"
    WASTE_05_07_99 = "05 07 99", "déchets non spécifiés ailleurs"
    WASTE_06_01_01 = "06 01 01*", "acide sulfurique et acide sulfureux"
    WASTE_06_01_02 = "06 01 02*", "acide chlorhydrique"
    WASTE_06_01_03 = "06 01 03*", "acide fluorhydrique"
    WASTE_06_01_04 = "06 01 04*", "acide phosphorique et acide phosphoreux"
    WASTE_06_01_05 = "06 01 05*", "acide nitrique et acide nitreux"
    WASTE_06_01_06 = "06 01 06*", "autres acides"
    WASTE_06_01_99 = "06 01 99", "déchets non spécifiés ailleurs"
    WASTE_06_02_01 = "06 02 01*", "hydroxyde de calcium"
    WASTE_06_02_03 = "06 02 03*", "hydroxyde d'ammonium"
    WASTE_06_02_04 = "06 02 04*", "hydroxyde de sodium et hydroxyde de potassium"
    WASTE_06_02_05 = "06 02 05*", "autres bases"
    WASTE_06_02_99 = "06 02 99", "déchets non spécifiés ailleurs"
    WASTE_06_03_11 = "06 03 11*", "sels et solutions contenant des cyanures"
    WASTE_06_03_13 = "06 03 13*", "sels et solutions contenant des métaux lourds"
    WASTE_06_03_14 = "06 03 14", "sels solides et solutions autres que ceux visés aux rubriques 06 03 11 et 06 03 13"
    WASTE_06_03_15 = "06 03 15*", "oxydes métalliques contenant des métaux lourds"
    WASTE_06_03_16 = "06 03 16", "oxydes métalliques autres que ceux visés à la rubrique 06 03 15"
    WASTE_06_03_99 = "06 03 99", "déchets non spécifiés ailleurs"
    WASTE_06_04_03 = "06 04 03*", "déchets contenant de l'arsenic"
    WASTE_06_04_04 = "06 04 04*", "déchets contenant du mercure"
    WASTE_06_04_05 = "06 04 05*", "déchets contenant d'autres métaux lourds"
    WASTE_06_04_99 = "06 04 99", "déchets non spécifiés ailleurs"
    WASTE_06_05_02 = (
        "06 05 02*",
        "boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_06_05_03 = (
        "06 05 03",
        "boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 06 05 02",
    )
    WASTE_06_06_02 = "06 06 02*", "déchets contenant des sulfures dangereux"
    WASTE_06_06_03 = "06 06 03", "déchets contenant des sulfures autres que ceux visés à la rubrique 06 06 02"
    WASTE_06_06_99 = "06 06 99", "déchets non spécifiés ailleurs"
    WASTE_06_07_01 = "06 07 01*", "déchets contenant de l'amiante provenant de l'électrolyse"
    WASTE_06_07_02 = "06 07 02*", "déchets de charbon actif utilisé pour la production du chlore"
    WASTE_06_07_03 = "06 07 03*", "boues de sulfate de baryum contenant du mercure"
    WASTE_06_07_04 = "06 07 04*", "solutions et acides, par exemple acide de contact"
    WASTE_06_07_99 = "06 07 99", "déchets non spécifiés ailleurs"
    WASTE_06_08_02 = "06 08 02*", "déchets contenant des chlorosilanes dangereux"
    WASTE_06_08_99 = "06 08 99", "déchets non spécifiés ailleurs"
    WASTE_06_09_02 = "06 09 02", "scories phosphoriques"
    WASTE_06_09_03 = (
        "06 09 03*",
        "déchets de réactions basées sur le calcium contenant des substances dangereuses ou contaminées par de telles substances",
    )
    WASTE_06_09_04 = (
        "06 09 04",
        "déchets de réactions basées sur le calcium autres que ceux visés à la rubrique 06 09 03",
    )
    WASTE_06_09_99 = "06 09 99", "déchets non spécifiés ailleurs"
    WASTE_06_10_02 = "06 10 02*", "déchets contenant des substances dangereuses"
    WASTE_06_10_99 = "06 10 99", "déchets non spécifiés ailleurs"
    WASTE_06_11_01 = (
        "06 11 01",
        "déchets de réactions basées sur le calcium provenant de la production de dioxyde de titane",
    )
    WASTE_06_11_99 = "06 11 99", "déchets non spécifiés ailleurs"
    WASTE_06_13_01 = (
        "06 13 01*",
        "produits phytosanitaires inorganiques, agents de protection du bois et autres biocides",
    )
    WASTE_06_13_02 = "06 13 02*", "charbon actif usé (sauf rubrique 06 07 02)"
    WASTE_06_13_03 = "06 13 03", "noir de carbone"
    WASTE_06_13_04 = "06 13 04*", "déchets provenant de la transformation de l'amiante"
    WASTE_06_13_05 = "06 13 05*", "suies"
    WASTE_06_13_99 = "06 13 99", "déchets non spécifiés ailleurs"
    WASTE_07_01_01 = "07 01 01*", "eaux de lavage et liqueurs mères aqueuses"
    WASTE_07_01_03 = "07 01 03*", "solvants, liquides de lavage et liqueurs mères organiques halogénés"
    WASTE_07_01_04 = "07 01 04*", "autres solvants, liquides de lavage et liqueurs mères organiques"
    WASTE_07_01_07 = "07 01 07*", "résidus de réaction et résidus de distillation halogénés"
    WASTE_07_01_08 = "07 01 08*", "autres résidus de réaction et résidus de distillation"
    WASTE_07_01_09 = "07 01 09*", "gâteaux de filtration et absorbants usés halogénés"
    WASTE_07_01_10 = "07 01 10*", "autres gâteaux de filtration et absorbants usés"
    WASTE_07_01_11 = (
        "07 01 11*",
        "boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_07_01_12 = (
        "07 01 12",
        "boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 07 01 11",
    )
    WASTE_07_01_99 = "07 01 99", "déchets non spécifiés ailleurs"
    WASTE_07_02_01 = "07 02 01*", "eaux de lavage et liqueurs mères aqueuses"
    WASTE_07_02_03 = "07 02 03*", "solvants, liquides de lavage et liqueurs mères organiques halogénés"
    WASTE_07_02_04 = "07 02 04*", "autres solvants, liquides de lavage et liqueurs mères organiques"
    WASTE_07_02_07 = "07 02 07*", "résidus de réaction et résidus de distillation halogénés"
    WASTE_07_02_08 = "07 02 08*", "autres résidus de réaction et résidus de distillation"
    WASTE_07_02_09 = "07 02 09*", "gâteaux de filtration et absorbants usés halogénés"
    WASTE_07_02_10 = "07 02 10*", "autres gâteaux de filtration et absorbants usés"
    WASTE_07_02_11 = (
        "07 02 11*",
        "boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_07_02_12 = (
        "07 02 12",
        "boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 07 02 11",
    )
    WASTE_07_02_13 = "07 02 13", "déchets plastiques"
    WASTE_07_02_14 = "07 02 14*", "déchets provenant d'additifs contenant des substances dangereuses"
    WASTE_07_02_15 = "07 02 15", "déchets provenant d'additifs autres que ceux visés à la rubrique 07 02 14"
    WASTE_07_02_16 = "07 02 16*", "déchets contenant des silicones dangereux"
    WASTE_07_02_17 = "07 02 17", "déchets contenant des silicones autres que ceux visés à la rubrique 07 02 16"
    WASTE_07_02_99 = "07 02 99", "déchets non spécifiés ailleurs"
    WASTE_07_03_01 = "07 03 01*", "eaux de lavage et liqueurs mères aqueuses"
    WASTE_07_03_03 = "07 03 03*", "solvants, liquides de lavage et liqueurs mères organiques halogénés"
    WASTE_07_03_04 = "07 03 04*", "autres solvants, liquides de lavage et liqueurs mères organiques"
    WASTE_07_03_07 = "07 03 07*", "résidus de réaction et résidus de distillation halogénés"
    WASTE_07_03_08 = "07 03 08*", "autres résidus de réaction et résidus de distillation"
    WASTE_07_03_09 = "07 03 09*", "gâteaux de filtration et absorbants usés halogénés"
    WASTE_07_03_10 = "07 03 10*", "autres gâteaux de filtration et absorbants usés"
    WASTE_07_03_11 = (
        "07 03 11*",
        "boues provenant du traitement in situ des effluents contenant des substances dangereuses",
    )
    WASTE_07_03_12 = (
        "07 03 12",
        "boues provenant du traitement in situ des effluents autres que celles visées à la rubrique 07 03 11",
    )
    WASTE_07_03_99 = "07 03 99", "déchets non spécifiés ailleurs"
    WASTE_07_04_01 = "07 04 01*", "eaux de lavage et liqueurs mères aqueuses"
