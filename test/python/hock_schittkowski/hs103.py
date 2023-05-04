# This is an automatically generated file converting from the apm format
import casadi as cs


def hs103():
    # The optimal objective is (if given in):
    f_opt = 543.667958
    x_opt = cs.DM([4.3941, 0.854469, 2.84323, 3.39998, 0.722926, 0.870406, 0.0246388])
    x = cs.MX.sym('x', 7)
    x0 = cs.DM.zeros(7, 1)
    lbx = -cs.inf*cs.DM.ones(7, 1)
    ubx = cs.inf*cs.DM.ones(7, 1)
    l = cs.DM.zeros(7, 1)
    g = cs.MX.zeros(6, 1)
    lbg = -cs.inf*cs.DM.ones(6, 1)
    ubg = cs.inf*cs.DM.ones(6, 1)

    a = .5
    l[0:6] = 0.1
    l[6] = 0.01

    x0[0:7] = 6
    lbx[0:7] = l[0:7]
    ubx[0:7] = 10

    lbg[0] = 0
    g[0] = 1-.5*x[0]**0.5*x[6]/(x[2]*x[5]**2)-.7*x[0]**3*x[1]*x[5]*x[6]**.5/x[2]**2 -.2*x[2]*x[5]**(2/3)*x[6]**.25/(x[1]*x[3]**.5)
    lbg[1] = 0
    g[1] = 1-1.3*x[1]*x[5]/(x[0]**.5*x[2]*x[4])-.8*x[2]*x[5]**2/(x[3]*x[4]) -3.1*x[1]**.5*x[5]**(1/3)/(x[0]*x[3]**2*x[4])
    lbg[2] = 0
    g[2] = 1-2*x[0]*x[4]*x[6]**(1/3)/(x[2]**1.5*x[5])-.1*x[1]*x[4]/ (x[2]**.5*x[5]*x[6]**.5)-x[1]*x[2]**.5*x[4]/x[0]- .65*x[2]*x[4]*x[6]/(x[1]**2*x[5])
    lbg[3] = 0
    g[3] = 1-.2*x[1]*x[4]**.5*x[6]**(1/3)/(x[0]**2*x[3])-.3*x[0]**.5*x[1]**2 *x[2]*x[3]**(1/3)*x[6]**.25/x[4]**(2/3)-.4*x[2]*x[4]*x[6]**.75/ (x[0]**3*x[1]**2)-.5*x[3]*x[6]**.5/x[2]**2
    lbg[4] = 100
    g[4] = 10*x[0]*x[3]**2*x[6]**a/(x[1]*x[5]**3)+15*x[2] *x[3]/(x[0]*x[1]**2*x[4]*x[6]**0.5)+20*x[1]*x[5]/(x[0]**2*x[3]*x[4]**2) +25*x[0]**2*x[1]**2*x[4]**0.5*x[6]/(x[2]*x[5]**2)
    ubg[5] = 3000
    g[5] = 10*x[0]*x[3]**2*x[6]**a/(x[1]*x[5]**3)+15*x[2] *x[3]/(x[0]*x[1]**2*x[4]*x[6]**0.5)+20*x[1]*x[5]/(x[0]**2*x[3]*x[4]**2) +25*x[0]**2*x[1]**2*x[4]**0.5*x[6]/(x[2]*x[5]**2)
    f = 10*x[0]*x[3]**2*x[6]**a/(x[1]*x[5]**3)+15*x[2] *x[3]/(x[0]*x[1]**2*x[4]*x[6]**0.5)+20*x[1]*x[5]/(x[0]**2*x[3]*x[4]**2) +25*x[0]**2*x[1]**2*x[4]**0.5*x[6]/(x[2]*x[5]**2)

    return (x_opt, f_opt, x, f, g, lbg, ubg, lbx, ubx, x0)
