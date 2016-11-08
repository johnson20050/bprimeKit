#*******************************************************************************
 #
 #  Filename    : bprimeKit_MC25ns_MiniAOD_76X.py
 #  Description : Default settings for DataProcessing Flag MC25ns_MiniAOD_76X
 #  Author      : Yi-Mu "Enoch" Chen [ ensc@hep1.phys.ntu.edu.tw ]
 #
 #  Ditching original cfg framework 2016-03
 #
#*******************************************************************************
import FWCore.ParameterSet.Config        as cms
import bpkFrameWork.bprimeKit.HLTStorage as myHLT
#-------------------------------------------------------------------------------
#   Tag settings
#-------------------------------------------------------------------------------

GlobalTag            = "80X_mcRun2_asymptotic_2016_miniAODv2_v1"
ElectronIDHEEPModule = "RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV60_cff"
ElectronIDModule     = "RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_V1_cff"


#-------------------------------------------------------------------------------
#   BprimeKit input settings
#-------------------------------------------------------------------------------
bprimeKit = cms.EDAnalyzer(
      "bprimeKit",
      #----- Operation Tags
      #----- Defined directly in cfg.py files
      MCtag           = cms.bool( False ),
      SkipGenInfo     = cms.bool( False ),
      PairCollection  = cms.int32(1),
      IncludeL7       = cms.bool(False),
      Debug           = cms.int32(0),
      runOnB2G        = cms.bool( False ),
      runMuonJetClean = cms.bool( True ),

      #----- Event level objects -----
      rhoLabel      = cms.InputTag( 'fixedGridRhoFastjetAll' ),
      metLabel      = cms.InputTag( 'slimmedMETs' ),
      puppimetLabel = cms.InputTag( 'slimmedMETsPuppi'),
      puInfoLabel = cms.InputTag( 'slimmedAddPileupInfo' ),

      #----- Trigger object storage -----
      hltLabel      = cms.InputTag( 'TriggerResults::HLT2' ),
      trgobjLabel  = cms.InputTag( 'selectedPatTrigger'),
      triggerlist  = myHLT.triggerlist,

      #----- Vertex related  ------------------------------------------------------------------------------
      offlinePVLabel   = cms.InputTag( 'offlineSlimmedPrimaryVertices' ),
      offlinePVBSLabel = cms.InputTag( 'offlinePrimaryVerticesWithBS' ),
      offlineBSLabel   = cms.InputTag( 'offlineBeamSpot' ),

      #----- MC Generation information --------------------------------------------------------------------
      genevtLabel = cms.InputTag( 'generator' ),
      genLabel    = cms.InputTag( 'prunedGenParticles' ),
      gtdigiLabel = cms.InputTag( 'gtDigis' ),
      lheLabel    = cms.InputTag( 'externalLHEProducer' ),
      lheRunLabel = cms.InputTag( 'externalLHEProducer' ),

      #----- Photon information ------------------------------------------------------------------------
      PhoCollections            = cms.vstring('PhotonInfo'),
      phoLabel                  = cms.VInputTag( 'slimmedPhotons' ),
      phoLooseIdMap             = cms.InputTag( 'egmPhotonIDs:cutBasedPhotonID-Spring15-50ns-V1-standalone-loose' ) ,
      phoMediumIdMap            = cms.InputTag( 'egmPhotonIDs:cutBasedPhotonID-Spring15-50ns-V1-standalone-medium') ,
      phoTightIdMap             = cms.InputTag( 'egmPhotonIDs:cutBasedPhotonID-Spring15-50ns-V1-standalone-tight') ,
      phoChargedIsolation       = cms.InputTag( "photonIDValueMapProducer:phoChargedIsolation"                          ) ,
      phoNeutralHadronIsolation = cms.InputTag( "photonIDValueMapProducer:phoNeutralHadronIsolation"                    ) ,
      phoPhotonIsolation        = cms.InputTag( "photonIDValueMapProducer:phoPhotonIsolation"                           ) ,
      full5x5SigmaIEtaIEtaMap   = cms.InputTag( "photonIDValueMapProducer:phoFull5x5SigmaIEtaIEta"),
      effAreaChHadFile          = cms.FileInPath("RecoEgamma/PhotonIdentification/data/PHYS14/effAreaPhotons_cone03_pfChargedHadrons_V2.txt"),
      effAreaNeuHadFile         = cms.FileInPath("RecoEgamma/PhotonIdentification/data/PHYS14/effAreaPhotons_cone03_pfNeutralHadrons_V2.txt"),
      effAreaPhoFile            = cms.FileInPath("RecoEgamma/PhotonIdentification/data/PHYS14/effAreaPhotons_cone03_pfPhotons_V2.txt"),

      #----- Lepton related information -------------------------------------------------------------------
      LepCollections  = cms.vstring( 'LepInfo'  ) ,
      muonLabel       = cms.VInputTag( 'slimmedMuons'     ) ,
      elecLabel       = cms.VInputTag( 'slimmedElectrons' ) ,
      tauLabel        = cms.VInputTag( 'slimmedTaus'      ) ,
      packedCand      = cms.InputTag( 'packedPFCandidates' ),
      eleVetoIdMap    = cms.InputTag( 'egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto'  ) ,
      eleLooseIdMap   = cms.InputTag( 'egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose'  ) ,
      eleMediumIdMap  = cms.InputTag( 'egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium'  ) ,
      eleTightIdMap   = cms.InputTag( 'egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight'  ) ,
      eleHEEPIdMap    = cms.InputTag( 'egmGsfElectronIDs:heepElectronID-HEEPV60'  ) ,
      conversionsLabel = cms.InputTag( 'reducedEgamma', 'reducedConversions' ),

      #----- Jet Information ------------------------------------------------------------------------------
      JetSettings = cms.VPSet(
         cms.PSet(
            jetCollection = cms.string( 'JetInfo' ),
            jetLabel      = cms.InputTag( 'selectedPatJetsAK4PFCHS' ),
            subjetLabel   = cms.InputTag(''), ## No tag for this collection..
            ),
         cms.PSet(
            jetCollection = cms.string( 'JetInfoPuppi' ),
            jetLabel      = cms.InputTag( 'selectedPatJetsAK4PFPuppi' ),
            subjetLabel   = cms.InputTag(''), ## No tag for this collection
            ),
         cms.PSet(
            jetCollection = cms.string( 'JetAK8Info' ),
            jetLabel      = cms.InputTag( 'selectedPatJetsAK8PFCHS' ),
            subjetLabel   = cms.InputTag( 'selectedPatJetsAK8PFCHSSoftDropPacked' ),
            ),
         cms.PSet(
            jetCollection = cms.string( 'JetCA8Info' ),
            jetLabel      = cms.InputTag( 'selectedPatJetsAK8PFCHS' ),
            subjetLabel   = cms.InputTag( 'patJetsCMSTopTagCHSPacked' ),
            ),
         cms.PSet(
            jetCollection = cms.string( 'JetAK8InfoPuppi' ),
            jetLabel      = cms.InputTag( 'selectedPatJetsAK8PFPuppi' ),
            subjetLabel   = cms.InputTag( 'selectedPatJetsAK8PFPuppiSoftDropPacked' ),
            ),
         cms.PSet(
            jetCollection = cms.string( 'JetCA8InfoPuppi' ),
            jetLabel      = cms.InputTag( 'selectedPatJetsAK8PFPuppi' ),
            subjetLabel   = cms.InputTag( 'patJetsCMSTopTagPuppiPacked' ),
            ),
        )
      )
