"""Module for containing reference data for JDFTx tags.

This module contains reference data for JDFTx tags, such as valid options for
functionals, pseudopotentials, etc.
"""

from __future__ import annotations

from pymatgen.io.jdftx.generic_tags import BoolTag, FloatTag, IntTag, StrTag, TagContainer

func_options = [
    "gga",  # Perdew-Burke-Ernzerhof GGA
    "gga-PBE",  # Perdew-Burke-Ernzerhof GGA
    "gga-PBEsol",  # Perdew-Burke-Ernzerhof GGA reparametrized for solids
    "gga-PW91",  # Perdew-Wang GGA
    "Hartree-Fock",  # Full exact exchange with no correlation
    # "hyb-HSE06",  # HSE06 'wPBEh' hybrid with 1/4 screened exact exchange
    # ^ Commented out due to bug in JDFTx, use (hyb-gga-HSE06) instead
    "hyb-HSE12",  # Reparametrized screened exchange functional for accuracy
    # (w=0.185 A^-1 and a=0.313)
    "hyb-HSE12s",  # Reparametrized screened exchange functional for k-point
    # convergence (w=0.408 A^-1 and a=0.425)
    "hyb-PBE0",  # Hybrid PBE with 1/4 exact exchange
    "lda",  # Perdew-Zunger LDA
    "lda-PW",  # Perdew-Wang LDA
    "lda-PW-prec",  # Perdew-Wang LDA with extended precision (used by PBE)
    "lda-PZ",  # Perdew-Zunger LDA
    "lda-Teter",  # Teter93 LSDA
    "lda-VWN",  # Vosko-Wilk-Nusair LDA
    "mgga-revTPSS",  # revised Tao-Perdew-Staroverov-Scuseria meta GGA
    "mgga-TPSS",  # Tao-Perdew-Staroverov-Scuseria meta GGA
    "orb-GLLBsc",  # Orbital-dependent GLLB-sc potential (no total energy)
    "pot-LB94",  # van Leeuwen-Baerends model potential (no total energy)
]

func_x_options = [
    "gga-x-2d-b86",  # Becke 86 in 2D
    "gga-x-2d-b86-mgc",  # Becke 86 with modified gradient correction for 2D
    "gga-x-2d-b88",  # Becke 88 in 2D
    "gga-x-2d-pbe",  # Perdew, Burke & Ernzerhof in 2D
    "gga-x-airy",  # Constantin et al based on the Airy gas
    "gga-x-ak13",  # Armiento & Kuemmel 2013
    "gga-x-am05",  # Armiento & Mattsson 05
    "gga-x-apbe",  # mu fixed from the semiclassical neutral atom
    "gga-x-b86",  # Becke 86
    "gga-x-b86-mgc",  # Becke 86 with modified gradient correction
    "gga-x-b86-r",  # Revised Becke 86 with modified gradient correction
    "gga-x-b88",  # Becke 88
    "gga-x-b88-6311g",  # Becke 88 reoptimized with the 6-311G** basis set
    "gga-x-b88m",  # Becke 88 reoptimized to be used with tau1
    "gga-x-bayesian",  # Bayesian best fit for the enhancement factor
    "gga-x-bcgp",  # Burke, Cancio, Gould, and Pittalis
    "gga-x-beefvdw",  # BEEF-vdW exchange
    "gga-x-bpccac",  # BPCCAC (GRAC for the energy)
    "gga-x-c09x",  # C09x to be used with the VdW of Rutgers-Chalmers
    "gga-x-cap",  # Correct Asymptotic Potential
    "gga-x-chachiyo",  # Chachiyo exchange
    "gga-x-dk87-r1",  # dePristo & Kress 87 version R1
    "gga-x-dk87-r2",  # dePristo & Kress 87 version R2
    "gga-x-eb88",  # Non-empirical (excogitated) B88 functional of Becke and
    # Elliott
    "gga-x-ecmv92",  # Engel, Chevary, Macdonald and Vosko
    "gga-x-ev93",  # Engel and Vosko
    "gga-x-fd-lb94",  # Functional derivative recovered from the stray LB94
    # potential
    "gga-x-fd-revlb94",  # Revised FD_LB94
    "gga-x-ft97-a",  # Filatov & Thiel 97 (version A)
    "gga-x-ft97-b",  # Filatov & Thiel 97 (version B)
    "gga-x-g96",  # Gill 96
    "gga-x-gam",  # Minnesota GAM exchange functional
    "gga-x-gg99",  # Gilbert and Gill 1999
    "gga-x-hcth-a",  # HCTH-A
    "gga-x-herman",  # Herman Xalphabeta GGA
    "gga-x-hjs-b88",  # HJS screened exchange B88 version
    "gga-x-hjs-b88-v2",  # HJS screened exchange B88 corrected version
    "gga-x-hjs-b97x",  # HJS screened exchange B97x version
    "gga-x-hjs-pbe",  # HJS screened exchange PBE version
    "gga-x-hjs-pbe-sol",  # HJS screened exchange PBE_SOL version
    "gga-x-htbs",  # Haas, Tran, Blaha, and Schwarz
    "gga-x-ityh",  # Short-range recipe for B88 functional - erf
    "gga-x-ityh-optx",  # Short-range recipe for OPTX functional
    "gga-x-ityh-pbe",  # Short-range recipe for PBE functional
    "gga-x-kgg99",  # Gilbert and Gill 1999 (mixed)
    "gga-x-kt1",  # Exchange part of Keal and Tozer version 1
    "gga-x-lag",  # Local Airy Gas
    "gga-x-lambda-ch-n",  # lambda_CH(N) version of PBE
    "gga-x-lambda-lo-n",  # lambda_LO(N) version of PBE
    "gga-x-lambda-oc2-n",  # lambda_OC2(N) version of PBE
    "gga-x-lb",  # van Leeuwen & Baerends
    "gga-x-lbm",  # van Leeuwen & Baerends modified
    "gga-x-lg93",  # Lacks & Gordon 93
    "gga-x-lspbe",  # lsPBE, a PW91-like modification of PBE exchange
    "gga-x-lsrpbe",  # lsRPBE, a PW91-like modification of RPBE
    "gga-x-lv-rpw86",  # Berland and Hyldgaard
    "gga-x-mb88",  # Modified Becke 88 for proton transfer
    "gga-x-mpbe",  # Adamo & Barone modification to PBE
    "gga-x-mpw91",  # mPW91 of Adamo & Barone
    "gga-x-n12",  # Minnesota N12 exchange functional
    "gga-x-ncap",  # Nearly correct asymptotic potential
    "gga-x-ncapr",  # Nearly correct asymptotic potential revised
    "gga-x-ol2",  # Exchange form based on Ou-Yang and Levy v.2
    "gga-x-optb86b-vdw",  # Becke 86 reoptimized for use with vdW functional
    # of Dion et al
    "gga-x-optb88-vdw",  # opt-Becke 88 for vdW
    "gga-x-optpbe-vdw",  # Reparametrized PBE for vdW
    "gga-x-optx",  # Handy & Cohen OPTX 01
    "gga-x-pbe",  # Perdew, Burke & Ernzerhof
    "gga-x-pbe-gaussian",  # Perdew, Burke & Ernzerhof with parameter values
    # used in Gaussian
    "gga-x-pbe-jsjr",  # Reparametrized PBE by Pedroza, Silva & Capelle
    "gga-x-pbe-mod",  # Perdew, Burke & Ernzerhof with less precise value for
    # beta
    "gga-x-pbe-mol",  # Reparametrized PBE by del Campo, Gazquez, Trickey & Vela
    "gga-x-pbe-r",  # Revised PBE from Zhang & Yang
    "gga-x-pbe-sol",  # Perdew, Burke & Ernzerhof SOL
    "gga-x-pbe-tca",  # PBE revised by Tognetti et al
    "gga-x-pbea",  # Madsen 07
    "gga-x-pbefe",  # PBE for formation energies
    "gga-x-pbeint",  # PBE for hybrid interfaces
    "gga-x-pbek1-vdw",  # Reparametrized PBE for vdW
    "gga-x-pbepow",  # PBE power
    "gga-x-pbetrans",  # Gradient-regulated connection-based correction for the
    # PBE exchange
    "gga-x-pw86",  # Perdew & Wang 86
    "gga-x-pw91",  # Perdew & Wang 91
    "gga-x-pw91-mod",  # PW91, alternate version with more digits
    "gga-x-q1d",  # Functional for quasi-1D systems
    "gga-x-q2d",  # Chiodo et al
    "gga-x-revssb-d",  # Revised Swart, Sola and Bickelhaupt dispersion
    "gga-x-rge2",  # Regularized PBE
    "gga-x-rpbe",  # Hammer, Hansen, and Norskov
    "gga-x-rpw86",  # Refitted Perdew & Wang 86
    "gga-x-s12g",  # Swart 2012 GGA exchange
    "gga-x-sfat",  # Short-range recipe for B88 functional - Yukawa
    "gga-x-sfat-pbe",  # Short-range recipe for PBE functional - Yukawa
    "gga-x-sg4",  # Semiclassical GGA at fourth order
    "gga-x-sogga",  # Second-order generalized gradient approximation
    "gga-x-sogga11",  # Second-order generalized gradient approximation 2011
    "gga-x-ssb",  # Swart, Sola and Bickelhaupt
    "gga-x-ssb-d",  # Swart, Sola and Bickelhaupt dispersion
    "gga-x-ssb-sw",  # Swart, Sola and Bickelhaupt correction to PBE
    "gga-x-vmt-ge",  # Vela, Medel, and Trickey with mu = mu_GE
    "gga-x-vmt-pbe",  # Vela, Medel, and Trickey with mu = mu_PBE
]

func_c_options = [
    "c-none",  # no correlation
    "gga-c-acgga",  # acGGA, asymptotically corrected GGA correlation
    "gga-c-acggap",  # acGGA+, asymptotically corrected GGA correlation+
    "gga-c-am05",  # Armiento & Mattsson 05
    "gga-c-apbe",  # mu fixed from the semiclassical neutral atom
    "gga-c-bmk",  # Boese-Martin correlation for kinetics
    "gga-c-ccdf",  # ccDF: coupled-cluster motivated density functional
    "gga-c-chachiyo",  # Chachiyo simple GGA correlation
    "gga-c-cs1",  # A dynamical correlation functional
    "gga-c-ft97",  # Filatov & Thiel correlation
    "gga-c-gam",  # Minnesota GAM correlation functional
    "gga-c-gapc",  # GapC
    "gga-c-gaploc",  # Gaploc
    "gga-c-hcth-a",  # HCTH-A
    "gga-c-lm",  # Langreth & Mehl
    "gga-c-lyp",  # Lee, Yang & Parr
    "gga-c-lypr",  # Short-range LYP by Ai, Fang, and Su
    "gga-c-mggac",  # beta fitted to LC20 to be used with MGGAC
    "gga-c-n12",  # Minnesota N12 correlation functional
    "gga-c-n12-sx",  # Minnesota N12-SX correlation functional
    "gga-c-op-b88",  # one-parameter progressive functional (B88 version)
    "gga-c-op-g96",  # one-parameter progressive functional (G96 version)
    "gga-c-op-pbe",  # one-parameter progressive functional (PBE version)
    "gga-c-op-pw91",  # one-parameter progressive functional (PW91 version)
    "gga-c-op-xalpha",  # one-parameter progressive functional (Xalpha version)
    "gga-c-optc",  # Optimized correlation functional of Cohen and Handy
    "gga-c-p86",  # Perdew 86
    "gga-c-p86-ft",  # Perdew 86 with more accurate value for ftilde
    "gga-c-p86vwn",  # Perdew 86 based on VWN5 correlation
    "gga-c-p86vwn-ft",  # Perdew 86 based on VWN5 correlation, with more
    # accurate value for ftilde
    "gga-c-pbe",  # Perdew, Burke & Ernzerhof
    "gga-c-pbe-gaussian",  # Perdew, Burke & Ernzerhof with parameters from
    # Gaussian
    "gga-c-pbe-jrgx",  # Reparametrized PBE by Pedroza, Silva & Capelle
    "gga-c-pbe-mol",  # Reparametrized PBE by del Campo, Gazquez, Trickey & Vela
    "gga-c-pbe-sol",  # Perdew, Burke & Ernzerhof SOL
    "gga-c-pbe-vwn",  # Perdew, Burke & Ernzerhof based on VWN correlation
    "gga-c-pbefe",  # PBE for formation energies
    "gga-c-pbeint",  # PBE for hybrid interfaces
    "gga-c-pbeloc",  # Semilocal dynamical correlation
    "gga-c-pw91",  # Perdew & Wang 91
    "gga-c-q2d",  # Chiodo et al
    "gga-c-regtpss",  # regularized TPSS correlation
    "gga-c-revtca",  # Tognetti, Cortona, Adamo (revised)
    "gga-c-rge2",  # Regularized PBE
    "gga-c-scan-e0",  # GGA component of SCAN
    "gga-c-sg4",  # Semiclassical GGA at fourth order
    "gga-c-sogga11",  # Second-order generalized gradient approximation 2011
    "gga-c-sogga11-x",  # To be used with HYB_GGA_X_SOGGA11_X
    "gga-c-spbe",  # PBE correlation to be used with the SSB exchange
    "gga-c-tau-hcth",  # correlation part of tau-hcth
    "gga-c-tca",  # Tognetti, Cortona, Adamo
    "gga-c-tm-lyp",  # Takkar and McCarthy reparametrization
    "gga-c-tm-pbe",  # Thakkar and McCarthy reparametrization
    "gga-c-w94",  # Wilson 94 (Eq. 25)
    "gga-c-wi",  # Wilson & Ivanov
    "gga-c-wi0",  # Wilson & Ivanov initial version
    "gga-c-wl",  # Wilson & Levy
    "gga-c-xpbe",  # Extended PBE by Xu & Goddard III
    "gga-c-zpbeint",  # spin-dependent gradient correction to PBEint
    "gga-c-zpbesol",  # spin-dependent gradient correction to PBEsol
    "gga-c-zvpbeint",  # another spin-dependent correction to PBEint
    "gga-c-zvpbeloc",  # PBEloc variation with enhanced compatibility with
    # exact exchange
    "gga-c-zvpbesol",  # another spin-dependent correction to PBEsol
    "lda-c-1d-csc",  # Casula, Sorella & Senatore
    "lda-c-1d-loos",  # P-F _Loos correlation LDA
    "lda-c-2d-amgb",  # AMGB (for 2D systems)
    "lda-c-2d-prm",  # PRM (for 2D systems)
    "lda-c-br78",  # Brual & Rothstein 78
    "lda-c-chachiyo",  # Chachiyo simple 2 parameter correlation
    "lda-c-chachiyo-mod",  # Chachiyo simple 2 parameter correlation with
    # modified spin scaling
    "lda-c-gk72",  # Gordon and Kim 1972
    "lda-c-gl",  # Gunnarson & Lundqvist
    "lda-c-gombas",  # Gombas
    "lda-c-hl",  # Hedin & Lundqvist
    "lda-c-karasiev",  # Karasiev reparameterization of Chachiyo
    "lda-c-karasiev-mod",  # Karasiev reparameterization of Chachiyo
    "lda-c-lp96",  # Liu-Parr correlation
    "lda-c-mcweeny",  # McWeeny 76
    "lda-c-ml1",  # Modified LSD (version 1) of Proynov and Salahub
    "lda-c-ml2",  # Modified LSD (version 2) of Proynov and Salahub
    "lda-c-ob-pw",  # Ortiz & Ballone (PW parametrization)
    "lda-c-ob-pz",  # Ortiz & Ballone (PZ parametrization)
    "lda-c-ow",  # Optimized Wigner
    "lda-c-ow-lyp",  # Wigner with corresponding LYP parameters
    "lda-c-pk09",  # Proynov and Kong 2009
    "lda-c-pmgb06",  # Long-range LDA correlation functional
    "lda-c-pw",  # Perdew & Wang
    "lda-c-pw-mod",  # Perdew & Wang (modified)
    "lda-c-pw-rpa",  # Perdew & Wang (fit to the RPA energy)
    "lda-c-pz",  # Perdew & Zunger
    "lda-c-pz-mod",  # Perdew & Zunger (Modified)
    "lda-c-rc04",  # Ragot-Cortona
    "lda-c-rpa",  # Random Phase Approximation (RPA)
    "lda-c-rpw92",  # Ruggeri, Rios, and Alavi restricted fit
    "lda-c-upw92",  # Ruggeri, Rios, and Alavi unrestricted fit
    "lda-c-vbh",  # von Barth & Hedin
    "lda-c-vwn",  # Vosko, Wilk & Nusair (VWN5)
    "lda-c-vwn-1",  # Vosko, Wilk & Nusair (VWN1)
    "lda-c-vwn-2",  # Vosko, Wilk & Nusair (VWN2)
    "lda-c-vwn-3",  # Vosko, Wilk & Nusair (VWN3)
    "lda-c-vwn-4",  # Vosko, Wilk & Nusair (VWN4)
    "lda-c-vwn-rpa",  # Vosko, Wilk & Nusair (VWN5_RPA)
    "lda-c-w20",  # Xie, Wu, and Zhao interpolation ansatz without fitting
    # parameters
    "lda-c-wigner",  # Wigner
    "lda-c-xalpha",  # Slater's Xalpha
    "mgga-c-b88",  # Meta-GGA correlation by Becke
    "mgga-c-b94",  # Becke 1994 meta-GGA correlation
    "mgga-c-bc95",  # Becke correlation 95
    "mgga-c-cc",  # Self-interaction corrected correlation functional by
    # Schmidt et al
    "mgga-c-ccalda",  # Iso-orbital corrected LDA correlation by Lebeda et al
    "mgga-c-cs",  # Colle and Salvetti
    "mgga-c-dldf",  # Dispersionless Density Functional
    "mgga-c-hltapw",  # Half-and-half meta-LDAized PW correlation by Lehtola
    # and Marques
    "mgga-c-kcis",  # Krieger, Chen, Iafrate, and _Savin
    "mgga-c-kcisk",  # Krieger, Chen, and Kurth
    "mgga-c-m05",  # Minnesota M05 correlation functional
    "mgga-c-m05-2x",  # Minnesota M05-2X correlation functional
    "mgga-c-m06",  # Minnesota M06 correlation functional
    "mgga-c-m06-2x",  # Minnesota M06-2X correlation functional
    "mgga-c-m06-hf",  # Minnesota M06-HF correlation functional
    "mgga-c-m06-l",  # Minnesota M06-L correlation functional
    "mgga-c-m06-sx",  # Minnesota M06-SX correlation functional
    "mgga-c-m08-hx",  # Minnesota M08 correlation functional
    "mgga-c-m08-so",  # Minnesota M08-SO correlation functional
    "mgga-c-m11",  # Minnesota M11 correlation functional
    "mgga-c-m11-l",  # Minnesota M11-L correlation functional
    "mgga-c-mn12-l",  # Minnesota MN12-L correlation functional
    "mgga-c-mn12-sx",  # Minnesota MN12-SX correlation functional
    "mgga-c-mn15",  # Minnesota MN15 correlation functional
    "mgga-c-mn15-l",  # Minnesota MN15-L correlation functional
    "mgga-c-pkzb",  # Perdew, Kurth, Zupan, and Blaha
    "mgga-c-r2scan",  # Re-regularized SCAN correlation by Furness et al
    "mgga-c-r2scan01",  # Re-regularized SCAN correlation with larger value for
    # eta
    "mgga-c-r2scanl",  # Deorbitalized re-regularized SCAN (r2SCAN-L)
    # correlation
    "mgga-c-revm06",  # Revised Minnesota M06 correlation functional
    "mgga-c-revm06-l",  # Minnesota revM06-L correlation functional
    "mgga-c-revm11",  # Revised Minnesota M11 correlation functional
    "mgga-c-revscan",  # revised SCAN
    "mgga-c-revscan-vv10",  # REVSCAN + VV10 correlation
    "mgga-c-revtm",  # revised Tao and Mo 2016 exchange
    "mgga-c-revtpss",  # revised TPSS correlation
    "mgga-c-rmggac",  # Revised correlation energy for MGGAC exchange functional
    "mgga-c-rppscan",  # r++SCAN: rSCAN with uniform density limit and
    # coordinate scaling behavior
    "mgga-c-rregtm",  # Revised regTM correlation by Jana et al
    "mgga-c-rscan",  # Regularized SCAN correlation by Bartok and Yates
    "mgga-c-scan",  # SCAN correlation of Sun, Ruzsinszky, and Perdew
    "mgga-c-scan-rvv10",  # SCAN + rVV10 correlation
    "mgga-c-scan-vv10",  # SCAN + VV10 correlation
    "mgga-c-scanl",  # Deorbitalized SCAN (SCAN-L) correlation
    "mgga-c-scanl-rvv10",  # SCAN-L + rVV10 correlation
    "mgga-c-scanl-vv10",  # SCAN-L + VV10 correlation
    "mgga-c-tm",  # Tao and Mo 2016 correlation
    "mgga-c-tpss",  # Tao, Perdew, Staroverov & Scuseria
    "mgga-c-tpss-gaussian",  # Tao, Perdew, Staroverov & Scuseria with
    # parameters from Gaussian
    "mgga-c-tpssloc",  # Semilocal dynamical correlation
    "mgga-c-vsxc",  # VSXC (correlation part)
]


func_xc_options = [
    "gga-b97-3c",  # Becke 97-3c by Grimme et. al.
    "gga-b97-d",  # Becke 97-D
    "gga-b97-gga1",  # Becke 97 GGA-1
    "gga-beefvdw",  # BEEF-vdW exchange-correlation
    "gga-edf1",  # EDF1
    "gga-hcth-120",  # HCTH/120
    "gga-hcth-147",  # HCTH/147
    "gga-hcth-407",  # HCTH/407
    "gga-hcth-407p",  # HCTH/407+
    "gga-hcth-93",  # HCTH/93
    "gga-hcth-p14",  # HCTH p=1/4
    "gga-hcth-p76",  # HCTH p=7/6
    "gga-hle16",  # High local exchange 2016
    "gga-kt1",  # Keal and Tozer, version 1
    "gga-kt2",  # Keal and Tozer, version 2
    "gga-kt3",  # Keal and Tozer, version 3
    "gga-mohlyp",  # Functional for organometallic chemistry
    "gga-mohlyp2",  # Functional for barrier heights
    "gga-mpwlyp1w",  # mPWLYP1w
    "gga-ncap",  # NCAP exchange + P86 correlation
    "gga-oblyp-d",  # oBLYP-D functional of Goerigk and Grimme
    "gga-opbe-d",  # oPBE-D functional of Goerigk and Grimme
    "gga-opwlyp-d",  # oPWLYP-D functional of Goerigk and Grimme
    "gga-pbe1w",  # PBE1W
    "gga-pbelyp1w",  # PBELYP1W
    "gga-th-fc",  # Tozer and Handy v. FC
    "gga-th-fcfo",  # Tozer and Handy v. FCFO
    "gga-th-fco",  # Tozer and Handy v. FCO
    "gga-th-fl",  # Tozer and Handy v. FL
    "gga-th1",  # Tozer and Handy v. 1
    "gga-th2",  # Tozer and Handy v. 2
    "gga-th3",  # Tozer and Handy v. 3
    "gga-th4",  # Tozer and Handy v. 4
    "gga-vv10",  # Vydrov and Van Voorhis
    "gga-xlyp",  # XLYP
    "hyb-gga-apbe0",  # Hybrid based on APBE
    "hyb-gga-apf",  # APF hybrid functional
    "hyb-gga-b1lyp",  # B1LYP
    "hyb-gga-b1pw91",  # B1PW91
    "hyb-gga-b1wc",  # B1WC
    "hyb-gga-b3lyp",  # B3LYP
    "hyb-gga-b3lyp-mcm1",  # B3LYP-MCM1
    "hyb-gga-b3lyp-mcm2",  # B3LYP-MCM2
    "hyb-gga-b3lyp3",  # B3LYP with VWN functional 3 instead of RPA
    "hyb-gga-b3lyp5",  # B3LYP with VWN functional 5 instead of RPA
    "hyb-gga-b3lyps",  # B3LYP*
    "hyb-gga-b3p86",  # B3P86
    "hyb-gga-b3p86-nwchem",  # B3P86, NWChem version
    "hyb-gga-b3pw91",  # The original (ACM, B3PW91) hybrid of Becke
    "hyb-gga-b5050lyp",  # B5050LYP
    "hyb-gga-b97",  # Becke 97
    "hyb-gga-b97-1",  # Becke 97-1
    "hyb-gga-b97-1p",  # Version of B97 by Cohen and Handy
    "hyb-gga-b97-2",  # Becke 97-2
    "hyb-gga-b97-3",  # Becke 97-3
    "hyb-gga-b97-k",  # Boese-Martin for Kinetics
    "hyb-gga-bhandh",  # BHandH i.e. BHLYP
    "hyb-gga-bhandhlyp",  # BHandHLYP
    "hyb-gga-blyp35",  # BLYP35
    "hyb-gga-cam-b3lyp",  # CAM version of B3LYP
    "hyb-gga-cam-o3lyp",  # CAM-O3LYP
    "hyb-gga-cam-pbeh",  # CAM hybrid screened exchange PBE version
    "hyb-gga-cam-qtp-00",  # CAM-B3LYP re-tuned using ionization potentials of
    # water
    "hyb-gga-cam-qtp-01",  # CAM-B3LYP re-tuned using ionization potentials of
    # water
    "hyb-gga-cam-qtp-02",  # CAM-B3LYP re-tuned using ionization potentials of
    # water
    "hyb-gga-camh-b3lyp",  # CAM version of B3LYP, tuned for TDDFT
    "hyb-gga-camy-b3lyp",  # CAMY version of B3LYP
    "hyb-gga-camy-blyp",  # CAMY version of BLYP
    "hyb-gga-camy-pbeh",  # CAMY hybrid screened exchange PBE version
    "hyb-gga-cap0",  # Correct Asymptotic Potential hybrid
    "hyb-gga-case21",  # CASE21: Constrained And Smoothed semi-Empirical 2021
    # functional
    "hyb-gga-edf2",  # EDF2
    "hyb-gga-hapbe",  # Hybrid based in APBE and zvPBEloc
    "hyb-gga-hflyp",  # HF + LYP correlation
    "hyb-gga-hjs-b88",  # HJS hybrid screened exchange B88 version
    "hyb-gga-hjs-b97x",  # HJS hybrid screened exchange B97x version
    "hyb-gga-hjs-pbe",  # HJS hybrid screened exchange PBE version
    "hyb-gga-hjs-pbe-sol",  # HJS hybrid screened exchange PBE_SOL version
    "hyb-gga-hpbeint",  # hPBEint
    "hyb-gga-hse-sol",  # HSEsol
    "hyb-gga-hse03",  # HSE03
    "hyb-gga-hse06",  # HSE06
    "hyb-gga-hse12",  # HSE12
    "hyb-gga-hse12s",  # HSE12 (short-range version)
    "hyb-gga-kmlyp",  # Kang-Musgrave hybrid
    "hyb-gga-lb07",  # Livshits and Baer, empirical functional also used for IP
    # tuning
    "hyb-gga-lc-blyp",  # LC version of BLYP
    "hyb-gga-lc-blyp-ea",  # LC version of BLYP for electron affinities
    "hyb-gga-lc-blypr",  # LC version of BLYP with correlation only in the
    # short range
    "hyb-gga-lc-bop",  # LC version of B88
    "hyb-gga-lc-pbeop",  # LC version of PBE
    "hyb-gga-lc-qtp",  # CAM-B3LYP re-tuned using ionization potentials of water
    "hyb-gga-lc-vv10",  # Vydrov and Van Voorhis
    "hyb-gga-lc-wpbe",  # Long-range corrected PBE (LC-wPBE) by Vydrov and
    # Scuseria
    "hyb-gga-lc-wpbe-whs",  # Long-range corrected PBE (LC-wPBE) by Weintraub,
    # Henderson and Scuseria
    "hyb-gga-lc-wpbe08-whs",  # Long-range corrected PBE (LC-wPBE) by Weintraub,
    # Henderson and Scuseria
    "hyb-gga-lc-wpbeh-whs",  # Long-range corrected short-range hybrid PBE
    # (LC-wPBE) by Weintraub, Henderson and Scuseria
    "hyb-gga-lc-wpbesol-whs",  # Long-range corrected PBE (LC-wPBE) by
    # Weintraub, Henderson and Scuseria
    "hyb-gga-lcy-blyp",  # LCY version of BLYP
    "hyb-gga-lcy-pbe",  # LCY version of PBE
    "hyb-gga-lrc-wpbe",  # Long-range corrected PBE (LRC-wPBE) by Rohrdanz,
    # Martins and Herbert
    "hyb-gga-lrc-wpbeh",  # Long-range corrected short-range hybrid PBE
    # (LRC-wPBEh) by Rohrdanz, Martins and Herbert
    "hyb-gga-mb3lyp-rc04",  # B3LYP with RC04 LDA
    "hyb-gga-mcam-b3lyp",  # Modified CAM-B3LYP by Day, Nguyen and Pachter
    "hyb-gga-mpw1k",  # mPW1K
    "hyb-gga-mpw1lyp",  # mPW1LYP
    "hyb-gga-mpw1pbe",  # mPW1PBE
    "hyb-gga-mpw1pw",  # mPW1PW
    "hyb-gga-mpw3lyp",  # MPW3LYP
    "hyb-gga-mpw3pw",  # MPW3PW of Adamo & Barone
    "hyb-gga-mpwlyp1m",  # MPW with 1 par. for metals/LYP
    "hyb-gga-o3lyp",  # O3LYP
    "hyb-gga-pbe-2x",  # PBE-2X: PBE0 with 56% exact exchange
    "hyb-gga-pbe-mol0",  # PBEmol0
    "hyb-gga-pbe-molb0",  # PBEmolbeta0
    "hyb-gga-pbe-sol0",  # PBEsol0
    "hyb-gga-pbe0-13",  # PBE0-1/3
    "hyb-gga-pbe38",  # PBE38: PBE0 with 3/8 = 37.5% exact exchange
    "hyb-gga-pbe50",  # PBE50
    "hyb-gga-pbeb0",  # PBEbeta0
    "hyb-gga-pbeh",  # PBEH (PBE0)
    "hyb-gga-qtp17",  # Global hybrid for vertical ionization potentials
    "hyb-gga-rcam-b3lyp",  # Similar to CAM-B3LYP, but trying to reduce the
    # many-electron self-interaction
    "hyb-gga-revb3lyp",  # Revised B3LYP
    "hyb-gga-sb98-1a",  # SB98 (1a)
    "hyb-gga-sb98-1b",  # SB98 (1b)
    "hyb-gga-sb98-1c",  # SB98 (1c)
    "hyb-gga-sb98-2a",  # SB98 (2a)
    "hyb-gga-sb98-2b",  # SB98 (2b)
    "hyb-gga-sb98-2c",  # SB98 (2c)
    "hyb-gga-tuned-cam-b3lyp",  # CAM version of B3LYP, tuned for excitations
    # and properties
    "hyb-gga-wb97",  # wB97 range-separated functional
    "hyb-gga-wb97x",  # wB97X range-separated functional
    "hyb-gga-wb97x-d",  # wB97X-D range-separated functional
    "hyb-gga-wb97x-d3",  # wB97X-D3 range-separated functional
    "hyb-gga-wb97x-v",  # wB97X-V range-separated functional
    "hyb-gga-wc04",  # Hybrid fitted to carbon NMR shifts
    "hyb-gga-whpbe0",  # Long-range corrected short-range hybrid PBE (whPBE0)
    # by Shao et al
    "hyb-gga-wp04",  # Hybrid fitted to proton NMR shifts
    "hyb-gga-x3lyp",  # X3LYP
    "hyb-lda-bn05",  # Baer and Neuhauser, gamma=1
    "hyb-lda-cam-lda0",  # CAM version of LDA0
    "hyb-lda-lda0",  # LDA hybrid exchange (LDA0)
    "hyb-mgga-b0kcis",  # Hybrid based on KCIS
    "hyb-mgga-b86b95",  # Mixture of B86 with BC95
    "hyb-mgga-b88b95",  # Mixture of B88 with BC95 (B1B95)
    "hyb-mgga-b94-hyb",  # Becke 1994 hybrid meta-GGA
    "hyb-mgga-b98",  # Becke 98
    "hyb-mgga-bb1k",  # Mixture of B88 with BC95 from Zhao and Truhlar
    "hyb-mgga-br3p86",  # BR3P86 hybrid meta-GGA from Neumann and Handy
    "hyb-mgga-edmggah",  # EDMGGA hybrid
    "hyb-mgga-lc-tmlyp",  # Long-range corrected TM-LYP by Jana et al
    "hyb-mgga-mpw1b95",  # Mixture of mPW91 with BC95 from Zhao and Truhlar
    "hyb-mgga-mpw1kcis",  # MPW1KCIS for barrier heights
    "hyb-mgga-mpwb1k",  # Mixture of mPW91 with BC95 for kinetics
    "hyb-mgga-mpwkcis1k",  # MPWKCIS1K for barrier heights
    "hyb-mgga-pbe1kcis",  # PBE1KCIS for binding energies
    "hyb-mgga-pw6b95",  # Mixture of PW91 with BC95 from Zhao and Truhlar
    "hyb-mgga-pw86b95",  # Mixture of PW86 with BC95
    "hyb-mgga-pwb6k",  # Mixture of PW91 with BC95 from Zhao and Truhlar for
    # kinetics
    "hyb-mgga-revtpssh",  # revTPSSh
    "hyb-mgga-tpss0",  # TPSS0 with 25% exact exchange
    "hyb-mgga-tpss1kcis",  # TPSS1KCIS for thermochemistry and kinetics
    "hyb-mgga-tpssh",  # TPSSh
    "hyb-mgga-wb97m-v",  # wB97M-V exchange-correlation functional
    "hyb-mgga-x1b95",  # Mixture of X with BC95
    "hyb-mgga-xb1k",  # Mixture of X with BC95 for kinetics
    "lda-1d-ehwlrg-1",  # LDA constructed from slab-like systems of 1 electron
    "lda-1d-ehwlrg-2",  # LDA constructed from slab-like systems of 2 electrons
    "lda-1d-ehwlrg-3",  # LDA constructed from slab-like systems of 3 electrons
    "lda-corrksdt",  # Corrected KSDT by Karasiev, Dufty and Trickey
    "lda-gdsmfb",  # _Groth, Dornheim, Sjostrom, Malone, Foulkes, Bonitz
    "lda-ksdt",  # Karasiev, Sjostrom, Dufty & Trickey
    "lda-lp-a",  # Lee-Parr reparametrization A
    "lda-lp-b",  # Lee-Parr reparametrization B
    "lda-teter93",  # Teter 93
    "lda-tih",  # Neural network LDA from Tozer et al
    "lda-zlp",  # Zhao, Levy & Parr, Eq. (20)
    "mgga-b97m-v",  # B97M-V exchange-correlation functional
    "mgga-cc06",  # Cancio and Chou 2006
    "mgga-hle17",  # High local exchange 2017
    "mgga-lp90",  # Lee & Parr, Eq. (56)
    "mgga-otpss-d",  # oTPSS-D functional of Goerigk and Grimme
    "mgga-tpsslyp1w",  # TPSSLYP1W
    "mgga-vcml-rvv10",  # VCML-rVV10 by Trepte and Voss
    "mgga-zlp",  # Zhao, Levy & Parr, Eq. (21)
]


jdftxdumpfreqoptions = ["Electronic", "End", "Fluid", "Gummel", "Init", "Ionic"]
jdftxdumpvaroptions = [
    "BandEigs",  # Band Eigenvalues
    "BandProjections",  # Projections of each band state against each
    # atomic orbital
    "BandUnfold",  # Unfold band structure from supercell to unit cell
    # (see command band-unfold)
    "Berry",  # Berry curvature i <dC/dk| X |dC/dk>, only allowed at End
    # (see command Cprime-params)
    "BGW",  # G-space wavefunctions, density and potential for Berkeley GW
    # (requires HDF5 support)
    "BoundCharge",  # Bound charge in the fluid
    "BulkEpsilon",  # Dielectric constant of a periodic solid
    # (see command bulk-epsilon)
    "ChargedDefect",  # Calculate energy correction for charged defect
    # (see command charged-defect)
    "CoreDensity",  # Total core electron density
    # (from partial core corrections)
    "Dfluid",  # Electrostatic potential due to fluid alone
    "Dipole",  # Dipole moment of explicit charges
    # (ionic and electronic)
    "Dn",  # First order change in electronic density
    "DOS",  # Density of States (see command density-of-states)
    "Dtot",  # Total electrostatic potential
    "Dvac",  # Electrostatic potential due to explicit system alone
    "DVext",  # External perturbation
    "DVscloc",  # First order change in local self-consistent potential
    "DWfns",  # Perturbation Wavefunctions
    "Ecomponents",  # Components of the energy
    "EigStats",  # Band eigenvalue statistics:
    # HOMO, LUMO, min, max and Fermi level
    "ElecDensity",  # Electronic densities (n or nup,ndn)
    "ElecDensityAccum",  # Electronic densities (n or nup,ndn)
    # accumulated over MD trajectory
    "EresolvedDensity",  # Electron density from bands within
    # specified energy ranges
    "ExcCompare",  # Energies for other exchange-correlation functionals
    # (see command elec-ex-corr-compare)
    "Excitations",  # Dumps dipole moments and transition strength
    # (electric-dipole) of excitations
    "FCI",  # Output Coulomb matrix elements in FCIDUMP format
    "FermiDensity",  # Electron density from fermi-derivative at
    # specified energy
    "FermiVelocity",  # Fermi velocity, density of states at Fermi
    # level and related quantities
    "Fillings",  # Fillings
    "FluidDebug",  # Fluid specific debug output if any
    "FluidDensity",  # Fluid densities (NO,NH,nWater for explicit fluids,
    # cavity function for PCMs)
    "Forces",  # Forces on the ions in the coordinate system selected by
    # command forces-output-coords
    "Gvectors",  # List of G vectors in reciprocal lattice basis,
    # for each k-point
    "IonicDensity",  # Nuclear charge density (with gaussians)
    "IonicPositions",  # Ionic positions in the same format
    # (and coordinate system) as the input file
    "KEdensity",  # Kinetic energy density of the valence electrons
    "Kpoints",  # List of reduced k-points in calculation,
    # and mapping to the unreduced k-point mesh
    "L",  # Angular momentum matrix elements, only allowed at End
    # (see command Cprime-params)
    "Lattice",  # Lattice vectors in the same format as the input file
    "Momenta",  # Momentum matrix elements in a binary file
    # (indices outer to inner: state, cartesian direction, band1, band2)
    "None",  # Dump nothing
    "Ocean",  # Wave functions for Ocean code
    "OrbitalDep",  # Custom output from orbital-dependent functionals
    # (eg. quasi-particle energies, discontinuity potential)
    "Q",  # Quadrupole r*p matrix elements, only allowed at End
    # (see command Cprime-params)
    "QMC",  # Blip'd orbitals and potential for CASINO [27]
    "R",  # Position operator matrix elements, only allowed at End
    # (see command Cprime-params)
    "RealSpaceWfns",  # Real-space wavefunctions (one column per file)
    "RhoAtom",  # Atomic-orbital projected density matrices
    # (only for species with +U enabled)
    "SelfInteractionCorrection",  # Calculates Perdew-Zunger self-interaction
    # corrected Kohn-Sham eigenvalues
    "SlabEpsilon",  # Local dielectric function of a slab
    # (see command slab-epsilon)
    "SolvationRadii",  # Effective solvation radii based on fluid bound charge
    # distribution
    "Spin",  # Spin matrix elements from non-collinear calculations in a
    # binary file (indices outer to inner: state, cartesian direction, band1,
    # # band2)
    "State",  # All variables needed to restart calculation: wavefunction and
    # fluid state/fillings if any
    "Stress",  # Dumps dE/dR_ij where R_ij is the i'th component of the
    # j'th lattice vector
    "Symmetries",  # List of symmetry matrices (in covariant lattice
    # coordinates)
    "Vcavity",  # Fluid cavitation potential on the electron density that
    # determines the cavity
    "Velocities",  # Diagonal momentum/velocity matrix elements in a binary
    # file (indices outer to inner: state, band, cartesian direction)
    "VfluidTot",  # Total contribution of fluid to the electron potential
    "Vlocps",  # Local part of pseudopotentials
    "Vscloc",  # Self-consistent potential
    "XCanalysis",  # Debug VW KE density, single-particle-ness and
    # spin-polarzied Hartree potential
]
# simple dictionaries deepcopied multiple times into MASTER_TAG_LIST later for
# different tags
jdftxminimize_subtagdict = {
    "alphaTincreaseFactor": FloatTag(),
    "alphaTmin": FloatTag(),
    "alphaTreduceFactor": FloatTag(),
    "alphaTstart": FloatTag(),
    "dirUpdateScheme": StrTag(
        options=[
            "FletcherReeves",
            "HestenesStiefel",
            "L-BFGS",
            "PolakRibiere",
            "SteepestDescent",
        ]
    ),
    "energyDiffThreshold": FloatTag(),
    "fdTest": BoolTag(),
    "history": IntTag(),
    "knormThreshold": FloatTag(),
    "linminMethod": StrTag(options=["CubicWolfe", "DirUpdateRecommended", "Quad", "Relax"]),
    "nAlphaAdjustMax": FloatTag(),
    "nEnergyDiff": IntTag(),
    "nIterations": IntTag(),
    "updateTestStepSize": BoolTag(),
    "wolfeEnergy": FloatTag(),
    "wolfeGradient": FloatTag(),
}
jdftxfluid_subtagdict = {
    "epsBulk": FloatTag(),
    "epsInf": FloatTag(),
    "epsLJ": FloatTag(),
    "Nnorm": FloatTag(),
    "pMol": FloatTag(),
    "poleEl": TagContainer(
        can_repeat=True,
        write_tagname=True,
        subtags={
            "omega0": FloatTag(write_tagname=False, optional=False),
            "gamma0": FloatTag(write_tagname=False, optional=False),
            "A0": FloatTag(write_tagname=False, optional=False),
        },
    ),
    # 'poleEl': FloatTag(can_repeat = True),
    "Pvap": FloatTag(),
    "quad_nAlpha": FloatTag(),
    "quad_nBeta": FloatTag(),
    "quad_nGamma": FloatTag(),
    "representation": TagContainer(subtags={"MuEps": FloatTag(), "Pomega": FloatTag(), "PsiAlpha": FloatTag()}),
    "Res": FloatTag(),
    "Rvdw": FloatTag(),
    "s2quadType": StrTag(
        options=[
            "10design60",
            "11design70",
            "12design84",
            "13design94",
            "14design108",
            "15design120",
            "16design144",
            "17design156",
            "18design180",
            "19design204",
            "20design216",
            "21design240",
            "7design24",
            "8design36",
            "9design48",
            "Euler",
            "Icosahedron",
            "Octahedron",
            "Tetrahedron",
        ]
    ),
    "sigmaBulk": FloatTag(),
    "tauNuc": FloatTag(),
    "translation": StrTag(options=["ConstantSpline", "Fourier", "LinearSpline"]),
}
