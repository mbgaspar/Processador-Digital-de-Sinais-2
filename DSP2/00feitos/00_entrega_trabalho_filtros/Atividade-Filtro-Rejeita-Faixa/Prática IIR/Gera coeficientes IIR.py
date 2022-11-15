from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np

def iir_sos_header(fname_out, SOS_mat):
    """
    Write IIR SOS Header Files
    File format is compatible with CMSIS-DSP IIR 
    Directform II Filter Functions
    
    Mark Wickert March 2015-October 2016
    """
    Ns, Mcol = SOS_mat.shape
    f = open(fname_out, 'wt')
    f.write('//define a IIR SOS CMSIS-DSP coefficient array\n\n')
    f.write('#include <stdint.h>\n\n')
    f.write('#ifndef STAGES\n')
    f.write('#define STAGES %d\n' % Ns)
    f.write('#endif\n')
    f.write('/*********************************************************/\n');
    f.write('/*                     IIR SOS Filter Coefficients       */\n');
    f.write('float32_t ba_coeff[%d] = { //b0,b1,b2,a1,a2,... by stage\n' % (5 * Ns))
    for k in range(Ns):
        if (k < Ns - 1):
            f.write('    %+-13e, %+-13e, %+-13e,\n' % \
                    (SOS_mat[k, 0], SOS_mat[k, 1], SOS_mat[k, 2]))
            f.write('    %+-13e, %+-13e,\n' % \
                    (-SOS_mat[k, 4], -SOS_mat[k, 5]))
        else:
            f.write('    %+-13e, %+-13e, %+-13e,\n' % \
                    (SOS_mat[k, 0], SOS_mat[k, 1], SOS_mat[k, 2]))
            f.write('    %+-13e, %+-13e\n' % \
                    (-SOS_mat[k, 4], -SOS_mat[k, 5]))
    # for k in range(Ns):
    #     if (k < Ns-1):
    #         f.write('    %15.12f, %15.12f, %15.12f,\n' % \
    #                 (SOS_mat[k,0],SOS_mat[k,1],SOS_mat[k,2]))
    #         f.write('    %15.12f, %15.12f,\n' % \
    #                 (-SOS_mat[k,4],-SOS_mat[k,5]))
    #     else:
    #         f.write('    %15.12f, %15.12f, %15.12f,\n' % \
    #                 (SOS_mat[k,0],SOS_mat[k,1],SOS_mat[k,2]))
    #         f.write('    %15.12f, %15.12f\n' % \
    #                 (-SOS_mat[k,4],-SOS_mat[k,5]))
    f.write('};\n')
    f.write('/*********************************************************/\n')
    f.close()


fs_kit=48000
fc=1300/(fs_kit/2)
delta=0.03

f1 = fc-delta
f2 = fc+delta

wp = [f1, f2]
ws = [f1+delta*0.8, f2-delta*0.8]
gpass = 1
gstop = 40

SOS = signal.iirdesign(wp, ws, gpass, gstop,output='sos')
w, h = signal.sosfreqz(SOS)

fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
#ax1.plot(w/np.pi, 20 * np.log10(abs(h)), 'b')
ax1.plot((w/np.pi)*(fs_kit/2), 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax1.grid()
ax1.set_ylim([-50, 5])
# ax2 = ax1.twinx()
# angles = np.unwrap(np.angle(h))
# ax2.plot(w, angles, 'g')
# ax2.set_ylabel('Angle (radians)', color='g')
# ax2.grid()
# ax2.axis('tight')
# ax2.set_ylim([-6, 1])
# nticks = 8
# ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
# ax2.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
plt.show()
iir_sos_header('coeff_IIR.h',SOS)
