from cffi import FFI
ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
enum linprog2d_status {
	LP2D_ERROR = 0,
	LP2D_INFEASIBLE = 1,
	LP2D_UNBOUNDED = 2,
	LP2D_EDGE = 3,
	LP2D_POINT = 4
};
struct linprog2d_result {
	double x1, y1, x2, y2;
	enum linprog2d_status status;
};
typedef struct linprog2d_result linprog2d_result_t;
linprog2d_result_t linprog2d_solve_simple(double cx, double cy, const double *Gx, const double *Gy, const double *h, unsigned int n);
""")

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_LP2d",
                      """
     #include "src/linprog2d.h" 
""",
                      sources=["src/linprog2d.c"],
                      libraries=['m'])   # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
