# ///////////////////////////////////////////////////////////////////////////////
# //        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
# //                        oscar.riveros@peqnp.science                        //
# //                                                                           //
# //   without any restriction, Oscar Riveros reserved rights, patents and     //
# //  commercialization of this knowledge or derived directly from this work.  //
# ///////////////////////////////////////////////////////////////////////////////
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Forrelation: A Problem that Optimally Separates Quantum from Classical Computing => https://arxiv.org/abs/1411.5729
# ref: https://www.quantamagazine.org/finally-a-problem-that-only-quantum-computers-will-ever-be-able-to-solve-20180621/

import numpy as np
from scipy.fft import fft


def hess(p, q, n):
    glb = np.inf
    seq = list(range(n))
    while True:
        ready = True
        for i in range(n):
            for j in range(n):
                while True:
                    seq[i], seq[j] = seq[j], seq[i]
                    loc = sum(fft(p) != q[seq])
                    if loc < glb:
                        glb = loc
                        print(glb)
                        if glb == 0:
                            return seq
                        ready = False
                    elif loc == glb:
                        break
        if ready:
            break
    return seq


def main():
    n = 100
    p = np.random.logistic(size=n)
    q = fft(p)
    np.random.shuffle(q)

    print(p)
    print(q)

    seq = hess(p, q, n)

    print('\nAre they related in a hidden way? {}\n'.format(fft(p) == q[seq]))

    print(fft(p))
    print(q[seq])


if __name__ == '__main__':
    main()
