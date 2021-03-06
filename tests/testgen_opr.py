
OperandSet = {
    'Ib' : { 
              '16' : ( "0x10", ), 
              '32' : ( "0x10", ), 
              '64' : ( "0x20", )  
    },
    'Eb_Gb' : { 
              '16' : ( "[bx+si], al", ), 
              '32' : ( "[eax+ebx], ch", "[ebx+ecx*4], bl", "[bx+0x10], dh"), 
              '64' : ( "[rax], r8b", )  
    },
    'Ev_Gv' : { 
              '16' : (), 
              '32' : ( "[eax+0x1234], esi", "[bx+si+0x1234], esp", "[esp+0x10], ebp"), 
              '64' : ()  
    },
    'Gb_Eb' : { 
              '16' : ( "al, bl", ), 
              '32' : ( "bl, cl", ), 
              '64' : ( "r8b, sil", )  
    },
    'Gv_Ev' : { 
              '16' : ( "ax, bx", ), 
              '32' : ( "eax, ebx", "ax, dx", "ax, [ebx+0x100]" ), 
              '64' : ( "rax, r15", "si, bp", "eax, edx" )  
    },
    'AL_Ib' : { 
              '16' : ( "al, 0x10", ), 
              '32' : ( "al, 0x13", ), 
              '64' : ( "al, 0x14", )  
    },
    'rAX_Iz' : { 
              '16' : ( "ax, 0x100", ), 
              '32' : ( "ax, 0x100", "eax, 0x100" ), 
              '64' : ( "r13, 0x200", )  
    },
    'Eb_Ib' : { 
              '16' : ( "al, 0x10", "byte [eax], 0x10" ), 
              '32' : ( "dl, 0x10", "byte [bp+si], 0x10" ), 
              '64' : ( "di, 0x10", "byte [rax+rsi], 0x10" )
    },
    'Ev_Iz' : { 
              '16' : ( "eax, 0x100000", "word [bx+si], 0x1000" ), 
              '32' : ( "eax, 0x100000", "word [bx+si], 0x1000", "dword [bp+0x10], 0x100" ), 
              '64' : ( "rax, 0x100000", "word [ebx+esi], 0x1000", "dword [ebp+0x10], 0x100" ), 
    },
    'Ev_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'V_W' : { 
              '16' : (), 
              '32' : ( "xmm3, xmm0", "xmm7, [eax]" ), 
              '64' : ( "xmm9, [rax+r8-0x10]", "xmm13, xmm1" )  
    },
    'V_VR' : { 
              '16' : (), 
              '32' : ( "xmm3, xmm0", "xmm7, xmm2" ), 
              '64' : ( "xmm9, xmm1", "xmm13, xmm1" )  
    },
    'Ew_Gw' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gv_Ed' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gv_M' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rAXr8' : { 
              '16' : (), 
              '32' : (), 
              '64' : ( "rax", "r8" )  
    },
    'rCXr9' : { 
              '16' : ( "ecx", ), 
              '32' : ( "ecx", ), 
              '64' : ( "r9", "rcx" )  
    },
    'rDXr10' : { 
              '16' : (), 
              '32' : (), 
              '64' : ( "r10", )  
    },
    'rBXr11' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rSPr12' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rBPr13' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rSIr14' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rDIr15' : { 
              '16' : (), 
              '32' : (), 
              '64' : ( "r15", "rdi" )  
    },
    'Ev' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ep' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Jz' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ap' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'M' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'V_W_Ib' : { 
              '16' : (), 
              '32' : ( "xmm0, xmm1, 0x10", ), 
              '64' : ( "xmm2, [r8+rdi+0x20], 0x28", )  
    },
    'P_W' : { 
              '16' : (), 
              '32' : ( "mm0, [eax]", "mm1, xmm0" ), 
              '64' : ()  
    },
    'V_Q' : { 
              '16' : (), 
              '32' : ( "xmm0, qword [eax]", ), 
              '64' : ( "xmm8, mm7", )  
    },
    'Gy_Wss' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
     },
    'Gy_Wsd' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gy_W' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'V_Ex' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eCX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eDX' : { 
              '16' : (), 
              '32' : ( "dx", "edx" ), 
              '64' : ( "edx", )  
    },
    'eBX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eSP' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eBP' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eSI' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eDI' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Eb' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Iw_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Mq' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Md' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST0_ST0' : { 
              '16' : (), 
              '32' : ( "st0, st0", ), 
              '64' : ()  
    },
    'ST1_ST0' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST2_ST0' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST3_ST0' : { 
              '16' : (), 
              '32' : ( "st3, st0", ), 
              '64' : ()  
    },
    'ST4_ST0' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST5_ST0' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST6_ST0' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST7_ST0' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST0_ST1' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST0_ST2' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST0_ST3' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST0_ST4' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST0_ST5' : { 
              '16' : (), 
              '32' : ( "st0, st5", ), 
              '64' : ()  
    },
    'ST0_ST6' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST0_ST7' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Mt' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST0' : { 
              '16' : (), 
              '32' : ( "st0", ), 
              '64' : ( "st1", )  
    },
    'ST1' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST2' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST3' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST4' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST5' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST6' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ST7' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Mw' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'AX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eAX_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'AL_DX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'eAX_DX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gv_Ev_Iz' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gv_Ev_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gd_Mo' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gq_Mo' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Jb' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gv_Ew' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'V_M' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gz_M' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ew' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'P_Q' : { 
              '16' : (), 
              '32' : ( "mm0, mm6", "mm1, [edi]" ), 
              '64' : ( "mm6, mm4", "mm7, [rax+rbx]" )  
    },
    'Ev_S' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'S_Ev' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'AL_Ob' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rAX_Ov' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ob_AL' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ov_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ALr8b_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'CLr9b_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'DLr10b_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'BLr11b_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'AHr12b_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'CHr13b_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'DHr14b_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'BHr15b_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rAXr8_Iv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rCXr9_Iv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rDXr10_Iv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rBXr11_Iv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rSPr12_Iv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rBPr13_Iv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rSIr14_Iv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rDIr15_Iv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'R_C' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'R_D' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'C_R' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'D_R' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'W_V' : { 
              '16' : ( "xmm3, [bx+si]", ), 
              '32' : (), 
              '64' : ( "xmm2, [rax+r8+0x10]", )  
    },
    'P_Ex' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ex_V' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ex_P' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'P_VR' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'M_V' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gd_VR' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'M_Gy' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'M_P' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Q_P' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'P_PR' : { 
              '16' : (), 
              '32' : ( "mm0, mm1", ), 
              '64' : ()  
    },
    'V_PR' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gv_Eb' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ib_AL' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ib_eAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'DX_AL' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'DX_eAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gd_VR_Ib' : { 
              '16' : (), 
              '32' : ( 'eax, xmm0, 0x3', ), 
              '64' : ( )  
    },
    'Gd_PR_Ib' : { 
              '16' : (), 
              '32' : ( 'eax, mm1, 0x9', ), 
              '64' : ()  
    },
    'P_Ew_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'V_Ew_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gd_PR' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'ES' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'SS' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'DS' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'GS' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'FS' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'P_Q_Ib' : { 
              '16' : (), 
              '32' : ( "mm0, mm1, 0xb", ), 
              '64' : ()  
    },
    'VR_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'PR_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'CS' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Iz' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Eb_I1' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Eb_CL' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ev_CL' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ev_I1' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Iw' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ev_Gv_Ib' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ev_Gv_CL' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'MwRv' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ed_Gd' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Eq_Gq' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gd_Ed' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Gq_Eq' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rAXr8_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rCXr9_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rDXr10_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rBXr11_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rSPr12_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rBPr13_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rSIr14_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'rDIr15_rAX' : { 
              '16' : (), 
              '32' : (), 
              '64' : ()  
    },
    'Ev_V_Ib' : { 
              '16' : (), 
              '32' : ( 'dword [eax], xmm0, 0x10', ), 
              '64' : ()  
    },
    'MbRv_V_Ib' : { 
              '16' : (), 
              '32' : ( 'byte [eax], xmm0, 0x10', ), 
              '64' : ()  
    },
    'MdRy_V_Ib' : { 
              '16' : (), 
              '32' : ( 'dword [eax], xmm0, 0x10', ), 
              '64' : ( 'rax, xmm2, 0x20', )  
    }
}
