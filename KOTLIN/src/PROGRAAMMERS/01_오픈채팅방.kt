package PROGRAAMMERS

fun main(){

    val record = arrayOf("Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan")

    println(record.joinToString(", "))

    solution(record)
}

private fun solution(record: Array<String>): Array<String> {
    var answer = arrayOf<String>()
    var msg = mapOf("Enter" to "님이 들어왔습니다.", "Leave" to "님이 나갔습니다.")
    println("${record.joinToString(", ")}")

    record.forEach {

    }


    return answer
}