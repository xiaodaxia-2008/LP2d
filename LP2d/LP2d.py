import cffi
from _LP2d import ffi
from _LP2d.lib import linprog2d_solve_simple, LP2D_EDGE, LP2D_POINT, LP2D_INFEASIBLE, LP2D_UNBOUNDED, LP2D_ERROR


def LP2dSolve(cx, cy, Gx, Gy, h, n):
    """
     minimize cx * x + cy * y
     w.r.t.   Gx[i] * x + Gy[i] * y >= h[i] for all 0 <= i < n

    Arguments:
        cx {[float]} -- [description]
        cy {[float]} -- [description]
        Gx {[np.array]} -- [description]
        Gy {[np.array]} -- [description]
        h {[np.array]} -- [description]
        n {[int]} -- [description]
    """
    pGx = ffi.cast("double*", Gx.ctypes.data)
    pGy = ffi.cast("double*", Gy.ctypes.data)
    ph = ffi.cast("double*", h.ctypes.data)
    return linprog2d_solve_simple(cx, cy, pGx, pGy, ph, n)
