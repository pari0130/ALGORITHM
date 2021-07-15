package STEP04

import java.util.*


// https://cote.inflearn.com/contest/10/problem/04-05
// 문자열 리스트 중 k번째 큰수 출력
/*
in
10 3
13 15 34 23 45 65 33 11 26 42

out
143
*/
private fun solution(arr: IntArray, n: Int = 0, k: Int): Int {
    val answer = -1
    val Tset = TreeSet(Collections.reverseOrder<Int>())
    for (i in 0 until n) {
        for (j in i + 1 until n) {
            for (l in j + 1 until n) {
                Tset.add(arr[i] + arr[j] + arr[l])
            }
        }
    }
    var cnt = 0
    //Tset.remove(143);
    //System.out.println(Tset.size());
    //System.out.println("first : "+ Tset.first());
    //System.out.println("last : "+ Tset.last());
    for (x in Tset) {
        //System.out.println(x);
        cnt++
        if (cnt == k) return x
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val k = kb.nextInt()
    val arr = IntArray(n)
    for (i in 0 until n) {
        arr[i] = kb.nextInt()
    }
    println(solution(arr, n, k))
}