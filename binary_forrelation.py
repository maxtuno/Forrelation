"""
///////////////////////////////////////////////////////////////////////////////
//        Copyright (c) 2012-2021 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
                    loc = sum(abs(fft(p[seq]) - q))
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
    n = 2 ** 7
    p = np.random.randint(0, 2, size=n)
    q = fft(p)
    np.random.shuffle(p)

    print(p)
    print(q)

    seq = hess(p, q, n)

    print('\nAre they related in a hidden way? {}\n'.format(fft(p[seq]) == q))

    print(fft(p))
    print(p[seq])


if __name__ == '__main__':
    main()
