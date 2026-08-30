"""Content for /handbook — the HCS Handbook 2026-2027.

Transcribed from the school's "Handbook_202627.docx" (revised 06/16/2026).
Each entry in SECTIONS becomes one <section> plus one entry in the sticky
contents list, so adding or reordering a section only means editing this list.
"""

SCHOOL_YEAR = "2026-2027"
REVISED = "Revised 06/16/2026"

STAFF = [
    ("Lower Learning Center Supervisor", "Mia Gilley"),
    ("Middle School Supervisor", "Grace Arnold"),
    ("Upper Learning Center Supervisor / Administrator", "Kevin Breau"),
]


# ---------------------------------------------------------------- helpers
def p(*paras):
    return "".join(f"<p>{t}</p>" for t in paras)


def ul(items, cls="hb-list"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items):
    return '<ol class="hb-steps">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def h3(t):
    return f"<h3>{t}</h3>"


def note(t, label="Note"):
    return f'<div class="hb-note"><strong>{label}</strong><p>{t}</p></div>'


def verse(text, ref):
    return f'<blockquote class="hb-verse"><p>{text}</p><cite>{ref}</cite></blockquote>'


def dl(pairs):
    rows = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in pairs)
    return f'<dl class="hb-defs">{rows}</dl>'


def fee_rows(rows):
    body = "".join(
        f'<div><span class="hb-fee__name">{n}</span><span class="hb-fee__amt">{a}</span></div>'
        for n, a in rows)
    return f'<div class="hb-fees">{body}</div>'


# ---------------------------------------------------------------- sections
INTRO = (
    p("Dear Parents/Guardians and Students,",
      "Welcome to our Hartland Christian School family! We thank you parents/guardians for entrusting your children to us for their formal education. We thank you students for coming to school with your great attitudes and excitement for a year of learning more about God&rsquo;s Word and God&rsquo;s world. With joy we look forward to the days ahead as we start a new year of learning both academically and spiritually.",
      "The handbook that follows is designed to set forth our policies in such a way as to help you have the most successful year possible. Our ultimate goal at HCS is that as the students make progress in their academics, we will consistently and lovingly address their heart issues and lead them into Christ-likeness. We understand that no external adherence to the policies set forth in the handbook is going to produce godliness. But every institution has to have its rules and regulations in order for things to run as smoothly as possible. We&rsquo;ve endeavored to base our standards on the unchanging principles found in God&rsquo;s Living Word, which instructs us in daily living so that we can live lives that are pleasing to Him.",
      "Training up children in the nurture and admonition of the Lord is an awesome task. Our prayer is that you will love God with all your heart, soul, and mind. He will delight in your willingness to serve Him &mdash; at home, at school, at church, and in your community. We commit to pray for you as you minister to your children. And we invite you to pray for us as we touch the hearts of your children for Christ&rsquo;s sake.")
    + '<p class="hb-signoff">Hartland Christian School Board</p>'
)

PURPOSE = (
    verse("Man&rsquo;s chief end is to glorify God and to enjoy Him forever.",
          "I Corinthians 6:20, Philippians 1:20, I Peter 4:11")
    + p("HCS has been an integral part of the ministry of First Baptist Church of Hartland, Maine since 1980, serving the surrounding communities for over 46 years. HCS was established to meet the need of the Christian community to assist in training of children in the teachings of the Bible as well as to provide an academic education in a Christian atmosphere by Christian teachers.",
        "The objective of this school is to enable students to become godly, well-trained, Christ-like leaders who will understand how to live out their faith in whatever arena God has for them.",
        "It&rsquo;s God&rsquo;s design that parents teach their children His Word. We seek to partner alongside you by teaching the academics along with Biblical truths and godly living.")
    + verse("Hear, O Israel: The LORD our God, the LORD is one! You shall love the LORD your God with all your heart, with all your soul, and with all your strength. And these words, which I command you today, shall be in your heart. You shall teach them diligently to your children, and shall talk of them when you sit in your house, when you walk by the way, when you lie down, and when you rise up.",
            "Deuteronomy 6:4-7")
    + h3("Doctrinal Statement")
    + p("HCS is a ministry of Hartland First Baptist Church, and as such, follows the same doctrinal statement as the church. Copies of the doctrinal statement are available upon request.")
    + h3("KJV Bible")
    + p("You will notice on your HCS Student Supply List that each grade is required to have a KJV Bible. This is not to say that we don&rsquo;t recognize the validity of some of the other versions. We require a KJV Bible because the curriculum that we use, A.C.E., exclusively uses this version. Having a KJV Bible will assist students in proper scoring of PACE work.")
)

ADMISSIONS = (
    p("HCS considers all applicants on the basis of their application form and does not discriminate on the basis of race, color, sex, or national origin.")
    + h3("Process")
    + ol(["Please read this handbook thoroughly.",
          "Complete and submit application form.",
          "Diagnostic Testing.",
          "Meet with School Board.",
          "Submit registration packet (include any transcript or medical records).",
          "Sign the Financial &amp; Handbook Policy Agreement.",
          "New students are given a probationary period of 30 days to see if the school is a proper fit. We are looking for a positive attitude and a willingness to work."])
    + p("We consider attendance at Hartland Christian School to be a privilege that we hope will reap positive, life-changing effects. We believe that a Christian education has the potential to affect all areas of life, not just academics.")
    + h3("Transfer Students")
    + p("Since A.C.E. is an individualized program that places each student at their current learning level, transfer students are required to take a placement test that covers Math, English, Word Building (Spelling), and Reading. The test recognizes what are called learning gaps which may be the result of a concept that the student didn&rsquo;t quite understand the first time that they were taught it or may be due to the fact that different curriculums teach things in a different order. Students are required to take the PACES that correspond to these learning gaps before they are allowed to start PACES at their current PACE level. Although it is a rare occurrence, sometimes a student will test far enough behind (3 years or more) that they may need to be placed in a lower grade. This is done to ensure that the student has adequate time to master concepts necessary for academic achievement.")
    + h3("High School Transfer Students")
    + p("High School transfer students are required to take the placement test as noted above. As long as they test past an 8th grade reading level, HCS will accept credits from the transferring High School. Any noted learning gaps will need to be completed. A student is required to complete at least 7 credits at HCS to be considered for a diploma.")
    + h3("Transfer Students from Another A.C.E. School or Home School")
    + p("Students transferring from another A.C.E. day school or A.C.E. home school that perform well on placement tests may be placed in the next consecutive PACE per their transcripts. However, if the staff notices that the student is unable to complete their work satisfactorily at the current PACE level, HCS reserves the right to retest and place the student at the PACE level warranted by the results of the test.")
    + h3("Standards for Admission Relating to Diagnostic Testing")
    + p("A student may not be admitted at grade level if they exceed a certain number of combined Math and English Gaps on the Diagnostic Test. A student entering Grade 12 is allowed only 10 Gaps. This number increases in increments of 5 for every grade below Grade 12.")
)

ATTENDANCE = (
    p("Attendance is required every day that school is in session as noted on the school calendar, which is distributed at the beginning of the school year. This includes any day that is set aside as a field trip or &ldquo;fun day.&rdquo; Students will be marked absent any day that they do not attend school. Unexcused absences of 15 days or more may result in dismissal from HCS.")
    + h3("Tardy")
    + p("Students are considered tardy if they&rsquo;re not in their Learning Centers by 8:30 a.m. Students must submit a written explanation for tardiness from their parents/guardians OR parents/guardians may verbally provide the explanation to a member of the staff. Either one must be accomplished on the day of the tardiness.")
    + h3("Absence")
    + p("Students must submit a written explanation for their absence on the first day they return to school. The following are excused absences:")
    + ul(["Illness of the student", "Critical illness in the family", "Death in the family",
          "Dental or medical appointments", "Special situations approved by the administration"])
    + h3("Early Dismissal")
    + p("Students who have their prescribed PACE work completed by the 8th week of the 4th quarter and are on grade level are granted permission to not attend the final week of school.")
    + h3("Ill Students")
    + p("In consideration of the other students and staff members, if your child is sick, has a fever, or has a loose or hacking cough, please keep him/her home. If he/she develops a fever or appears to be sick while at school we will call you to pick him/her up.")
    + h3("School Departure")
    + p("We consider the safety of the students a great responsibility. If your child is to go home with someone other than you (or your normally designated transportation), please let the staff know verbally or in writing.")
)

GENERAL = (
    dl([
        ("Closed Campus", "Students may not leave the school grounds during school hours without permission, except seniors who have earned senior privileges. Students&rsquo; guests may not come on the campus without the permission of the administration."),
        ("Deliveries", "Deliveries to students are to be left at the school office and will be given to the student at the next break."),
        ("Items From Home", "Students may bring items from home to school. Please show items to a staff member for approval. If an item is determined to be distracting or controversial, the student will be asked not to bring it to school again."),
        ("Prohibited Items", "Knives, guns, or any object the Administration decides is distracting or unsafe should not be brought to school."),
        ("Cell Phones &amp; Electronics", "Students may bring electronic devices (iPods, cameras, etc.) to school, BUT they may not have them in their possession during school hours. Students will give their electronic devices to the supervisor who will return them at the end of the day. If the student needs a device during the course of the day, he/she may request it from the supervisor."),
        ("Property", "Please treat school/church property with respect. Marked on, defaced, broken, or unreturned property, including athletic equipment, is to be replaced at the student&rsquo;s expense."),
        ("School Cancellation", "HCS will cancel when RSU 19 cancels due to weather or when circumstances dictate. School closings will be broadcast on TV &mdash; WLBZ (2) and WABI (5) and their websites. Cancellations will also be announced on the HCS Facebook page. Sports practices will be re-scheduled at the coach&rsquo;s discretion."),
        ("Social Events", "If your child is hosting a social event, he/she may pass out invitations to classmates at school during breaks."),
        ("Telephone Use", "The school phone is reserved for official school business and emergencies. Students who would like to make a call may request permission from the supervisor."),
        ("Transportation", "Please lock vehicles, including bikes."),
    ])
    + h3("Off Limits for Students")
    + ul(["Other students&rsquo; offices", "Teacher&rsquo;s Room",
          "Learning Center control and files", "Learning Center when staff is absent",
          "Gym, except under supervised activity or with permission",
          "Church Auditorium, except under supervised activity or with permission",
          "Vehicles", "Parking lot"], cls="hb-list hb-list--cols")
)

EXTRA = (
    h3("Church Attendance")
    + p("In our joint effort to raise up a godly generation, we encourage you to reinforce the same Biblical values in your home that we aspire to at the school. One way to do this is to attend a Bible-believing church with your children on a regular basis.")
    + h3("Christian Service")
    + p("We believe that God expects Christians to be ministering and serving one another. Therefore, we provide opportunities for Christian service to the students, such as:")
    + ul(["Music &amp; Drama, ministering to the First Baptist Church of Hartland and area churches.",
          "Devotions during morning assembly.",
          "Bible and Missions Stories."])
    + p("Students are encouraged to be involved in Christian Service outside of the school.",
        "Students are required to help with light chores such as shoveling walks or cleaning the kitchen after use, cleaning windows, offices, or gym at the close of each day. They will not use heavy acids or detergents. We want to teach them an attitude of willing, cheerful service &mdash; to do whatever they do as unto the Lord, for He looks on our hearts.")
    + verse("Whatever you do, do it heartily as unto the Lord.", "Colossians 3:23")
    + h3("Conquerors Sports Teams")
    + p("Volleyball for girls. Basketball for boys.",
        "Students in grades 6-12 who meet the requirements are eligible to play HCS Sports. We encourage students, staff, parents/guardians, friends and relatives to come to the games with good sportsmanship and cheer for the teams. We invite parents/guardians to help out in our snack shop.",
        "Parents of homeschooled students are required to provide evidence of sufficient academic progress tri-weekly to the Administrator in order to participate in athletics.")
    + h3("Participation on Public School Teams")
    + p("Students that are on Academic Balance and are at grade level that wish to participate in a sport that is not offered by HCS may participate in that sport at their local public school.")
    + dl([
        ("Off-Campus Activities", "Permission is given to students for afternoon off-campus activities providing he/she is on academic balance."),
        ("Field Trips", "To enhance the learning experience at HCS, various field trips are taken throughout the year. Permission slips will need to be on file."),
        ("HCS Boosters", "Our boosters program assists in fundraising as well as field trip planning for the school. We encourage all parents/guardians to join."),
    ])
)

CURRICULUM = (
    p("HCS utilizes the Accelerated Christian Education (A.C.E.) curriculum. Our Supervisors and Monitors are trained in this curriculum and are required to receive continuing education every year through A.C.E.&rsquo;s annual Educator&rsquo;s Convention.",
      "A.C.E. differs from a traditional school where classes are taught by a teacher. Students are individually prescribed curriculum and work at their own pace. Assisted by their Supervisors, students set goals each day that will enable them to complete their work in a timely fashion. Work is done in PACES. A PACE is a combination textbook/workbook; twelve PACES make up one grade level. Students score their own PACES. Tests are graded by Supervisors. Students are assigned offices (cubicles) instead of desks; this gives them a quiet space to complete their schoolwork. In addition to strong academics, A.C.E. encourages Scripture memorization. Most PACES have a verse to memorize before taking the test; verses relate to a character trait of Christ that&rsquo;s incorporated in the PACE. Also, a monthly Scripture passage (Administrator&rsquo;s choice) is assigned.",
      "A.C.E. believes in open communication between parents/guardians and Supervisors. HCS does as well. Supervisors are available by appointment or phone to answer questions.")
    + h3("Glossary of Terms")
    + dl([
        ("School Board", "Decides policy matters. Comprised by select members of the First Baptist Church of Hartland."),
        ("Administrator", "Like a principal, the Administrator is the final authority of the school. Mans the day-to-day operations, reports to the School Board, and assists in policy reform."),
        ("Supervisor", "Head teacher of respective classroom."),
        ("Monitor", "Assists the Supervisor in the classroom; similar to a teacher&rsquo;s aide."),
        ("Volunteers", "Help in extracurricular activities like hot lunch, art, and music. Held to the same standards as Supervisors and Monitors."),
        ("Learning Center", "Classroom."),
        ("Office", "The student&rsquo;s private area to complete work. Similar to a cubicle."),
        ("PACES", "Combination of textbook/workbook."),
        ("Academic Balance", "Minimum standard required to complete an entire grade level of curriculum if maintained throughout the school year. Each grade level generally includes twelve PACES per subject of required curriculum. Therefore, academic balance typically equates to the completion of three PACES per subject in each respective school year quarter. (Previously transferred students who are completing gap PACES may have to complete more than three PACES per quarter to reach their respective grade level.)"),
    ])
    + note("Report Cards are issued every Quarter (9 weeks) on the Friday after the Quarter ends.")
)

ORDER = (
    ol(["Pledges: American Flag, Christian Flag, Bible",
        "Devotions or Chapel",
        "PACE work",
        "Snack / Recess",
        "PACE work",
        "Lunch / Recess: 30 minutes",
        "PACE work and Electives (Art, Music, Gym, etc.)",
        "Recess"])
    + p("Students will be notified of the exact schedule at school orientation.")
    + h3("Recess")
    + p("Recess is supervised: in the gym or outside. During the winter months please provide appropriate cold weather attire.")
    + h3("Snack / Lunch")
    + ul(["Snack: mid-morning. Lunch: noontime.",
          "Students bring in their own snacks and lunches.",
          "Microwaves are available; due to the number of students needing to use microwaves, we ask that microwave meals take no more than 2 minutes.",
          "Students eat at the lunch tables in the gym. They may only eat in their classroom with the Supervisor&rsquo;s permission.",
          "Students may not share or trade food or drinks.",
          "Once done eating, students clean off their area of the table, place their trash in wastebaskets, and put their lunchbox away.",
          "Cartoon character lunch boxes are permitted; however, the Administration reserves the right to disallow any character considered inappropriate."])
)

DAILY = (
    h3("General")
    + p("Students raise a flag to request permission from the Supervisor or Monitor:")
    + ul(["To be out of their offices or to leave the classroom; includes restroom use.",
          "To do activities other than prescribed materials in their offices.",
          "To request help with academic questions."])
    + p("Students may use break time for such things as restroom use, sharpening pencils, and personal questions of staff or other students.")
    + h3("Student Offices")
    + ul(["The Supervisor assigns students&rsquo; offices.",
          "Students keep their own offices tidy.",
          "Students may arrange their offices with approved items such as a chair cushion, a desk mat, appropriate background material for the bulletin board.",
          "In addition to the Progress and Goal Charts, other items may be placed on the bulletin board. Please have the Supervisor or Monitor approve items before hanging them.",
          "Goal Chart is placed on the right-hand side of the bulletin board.",
          "Progress Card is placed on the left-hand side of the bulletin board. No marks are to be made on it ($1.00 charge for a replacement).",
          "The school provides students&rsquo; chairs. To avoid distraction, other chairs are not permitted (office chairs, etc.).",
          "You&rsquo;ll receive a list of supplies for your child to bring to school.",
          "Students are not to lean or sit on offices or on the dividers."])
    + h3("PACES")
    + p("PACE work is to be done in pencil. Goals are to be accomplished in this order:")
    + ol(["PACE tests", "Self-Tests", "Math OR English OR High School Sciences involving Math", "All other goals"])
    + ul(["Work must be shown for Math and Science (in the PACE or on scrap paper which then will be stapled to the page).",
          "Calculators are permitted once a student gets to Math PACE 1075 and the Supervisor is confident that the student has mastered basic math facts.",
          "PACES are private property and are not to be shared among students.",
          "PACES and textbooks should be maintained in a neat and orderly fashion. Textbooks and defaced or damaged PACES will be replaced at cost plus shipping and handling."])
    + h3("Goal Chart")
    + ul(["Students keep their Goal Charts up-to-date. Grades 7-12 must use a pen.",
          "Goal Charts are posted on the students&rsquo; bulletin boards (see &ldquo;Student Offices&rdquo; for details).",
          "Students write the exact page numbers they set for goals to work on that day.",
          "Students cross off daily goals once a PACE is scored and corrected."])
    + h3("Communication Slips")
    + ul(["Students are to deliver school communication to parents/guardians on the day it is received.",
          "Some communication slips must be signed and returned on the next day of school."])
    + h3("Scoring Station")
    + ul(["Score Keys are for scoring work only, not for finding the answers.",
          "Score Keys are to be handled carefully.",
          "Use the red pen supplied at the scoring station.",
          "Scoring is only to be done at the scoring station.",
          "Mark a red &ldquo;X&rdquo; beside wrong answers indicating to the Supervisor that you may need help.",
          "Write page numbers of where the answer is found next to each corrected answer on a checkup or self-test.",
          "Rescore, circling each &ldquo;X&rdquo; in red when the answer is correct. Continue the process until all answers are correct.",
          "Circle each PACE page number in red when all answers are correct on that page. This indicates that the page is finished and completely correct.",
          "Replace the Score Key and red pen in their proper place."])
    + h3("Scoring Violations")
    + p("It&rsquo;s the responsibility of the students to score their papers accurately. We realize that honest mistakes happen. We urge students to use care and not be hasty when scoring. It is considered cheating if:")
    + ul(["a pencil is taken to the scoring station, since it could be used to write in answers.",
          "a wrong answer is not marked with a red &ldquo;X.&rdquo;",
          "a page is circled complete when all corrections have not been made."])
    + h3("Checkups")
    + p("A checkup is essentially a self-exam (quiz) to see if the student is mastering the material.")
    + ul(["Students are not permitted to look back in the PACE for answers.",
          "Students must score an 80% or above on a checkup to proceed. Incorrect answers must be cross-referenced by recording the page number of the answer.",
          "A score of 79% or below: students will be quizzed before moving on or, at the Supervisor&rsquo;s discretion, repeat part of the previous section that hasn&rsquo;t been mastered."])
    + h3("Homework")
    + ul(["Students are issued homework slips if they have uncompleted goals or other assignments. Parents/guardians sign it. Students return it with completed homework the next school day.",
          "Homework is expected to be complete before students arrive at school the next school day.",
          "Homework is checked by one of the Monitors during the morning Goal Check.",
          "Students receive one demerit for each PACE containing unfinished homework."])
    + h3("Self-Test")
    + ul(["PACE must be initialed by Supervisor before starting Self-Test.",
          "A score of 90% or better: turn PACE in and take PACE Test.",
          "A score of 80%-89%: restudy and be quizzed before taking the PACE Test.",
          "A score below 80%: erase all checkups and Self-Test and retake them.",
          "Students must score an 80% or above before proceeding to the PACE Test."])
    + h3("PACE Test")
    + ul(["Once a PACE is completed and scored, students must turn the PACE in to be tested the next morning.",
          "Tests are administered at the Testing Table.",
          "Test time: one hour.",
          "A score of 80% or better: move on to the next PACE.",
          "A score below 80%: repeat the PACE (with a fee for a replacement PACE). Must score 80% or above on the retake PACE.",
          "The retake grade and the original grade will be averaged together for the final PACE grade. If the average is lower than 80%, the final grade will be 80%.",
          "If a student fails a PACE Test, he/she will be issued a note that must be signed by the parent/guardian and returned the next school day.",
          "Test results are given the next day of school. Then the next PACE will be issued. Exceptions are made at the Supervisor&rsquo;s discretion, e.g. when a student has limited time to get work done in time for graduation."])
)

PRIVILEGE_LEVELS = [
    ("Level A",
     ["Average 2 PACES a week", "Maintain Academic Balance",
      "Accumulate no more than 20 minutes of detention the previous week",
      "Memorize previous month&rsquo;s Scripture"],
     ["Extra 5 minutes morning break.",
      "May engage in approved extracurricular activities in office (convention prep., crafts, puzzles, games, etc.)"]),
    ("Level C",
     ["Average 2.5 PACES a week", "Maintain Academic Balance", "No detention previous week",
      "Memorize previous month&rsquo;s Scripture",
      "Present a monthly 3 minute oral report on an interest area or book report"],
     ["Extra 10 minutes morning break.",
      "May engage in approved extracurricular activities in office.",
      "May engage in extracurricular activities outside of office after last break in approved privilege areas.",
      "May be out of seat for a specific purpose without permission in learning center."]),
    ("Level E",
     ["Average 3 PACES a week", "Maintain Academic Balance", "No detention previous week",
      "Memorize previous month&rsquo;s Scripture",
      "Present a monthly 3 minute oral report on an interest area or book report",
      "Verified Monthly Christian Service, e.g. nursery helper, Jr. Church helper, usher. If Christian Service is done in a church other than ours, please verify by turning in a note from a person in charge of your service."],
     ["Extra 15 minutes morning break.",
      "May engage in approved extracurricular activities in office.",
      "May engage in extracurricular activities outside of office after 1:15 in approved privilege areas.",
      "May be out of seat for a specific purpose without permission in learning center.",
      "May engage in approved learning activities outside of office (e.g. music practice, educational software) at any time (must check out before leaving classroom)."]),
]

RESPONSIBILITIES = (
    p("We teach that acceptance of responsibility merits its own reward of greater privilege. Students at HCS will find this to be true through achieving A, C, or E privilege status.",
      "A student who has fulfilled his responsibilities may be on privilege status by submitting an Application for Privilege by Friday for the upcoming week.")
    + '<div class="hb-levels">'
    + "".join(f"""<div class="hb-level">
  <h3>{name}</h3>
  <h4>Responsibilities</h4>{ul(resp)}
  <h4>Privileges</h4>{ul(priv)}
</div>""" for name, resp, priv in PRIVILEGE_LEVELS)
    + "</div>"
    + h3("Senior Privileges")
    + p("Seniors may:")
    + ul(["go to a local store during breaks or lunch;",
          "finish school one week before graduation if on academic level and have finished course requirements;",
          "be dismissed at noon during the third and fourth quarters with parent&rsquo;s permission for the purpose of employment, if they have completed their course work for the day, are on Academic Level, and are forecasted by the Supervisor to complete required work by the end of the year."])
)

PROGRAMS = [
    ("Honors", "29", [("Math", "3.5"), ("English", "4.0"), ("Social Studies", "4.5"), ("Science", "4.0"),
                      ("Etymology", "1.0"), ("Bible Electives", "4.0"), ("Computer Science", "1.0"),
                      ("Keyboarding", "1.0"), ("Fine Arts Electives", "2.0"), ("Health Elective", "0.5"),
                      ("Language Electives", "2.0"), ("Other Electives", "1.5")]),
    ("College Prep", "26", [("Math", "3.0"), ("English", "4.0"), ("Social Studies", "4.5"), ("Science", "3.0"),
                            ("Etymology", "1.0"), ("Bible Electives", "4.0"), ("Computer Science", "1.0"),
                            ("Keyboarding", "1.0"), ("Fine Arts Electives", "1.5"), ("Health Elective", "0.5"),
                            ("Language Electives", "1.0"), ("Other Electives", "1.5")]),
    ("General Course", "24", [("Math", "2.0"), ("English", "4.0"), ("Social Studies", "4.5"), ("Science", "2.0"),
                              ("Etymology", "1.0"), ("Bible Electives", "4.0"), ("Computer Science", "1.0"),
                              ("Keyboarding", "1.0"), ("Fine Arts Electives", "1.0"), ("Health Elective", "0.5"),
                              ("Business Math", "1.0"), ("Other Electives", "2.0")]),
]


def _credit_table(name, total, rows):
    body = "".join(f"<tr><th scope='row'>{s}</th><td>{c}</td></tr>" for s, c in rows)
    return f"""<div class="hb-credits">
  <h4>{name} <span>Required credits: {total}</span></h4>
  <table><caption class="sr-only">{name} required credits</caption>
    <thead><tr><th scope="col">Subject</th><th scope="col">Cr</th></tr></thead>
    <tbody>{body}</tbody>
  </table>
</div>"""


COURSES = (
    ul(["To enter kindergarten: students must be five (5) years old by October 15.",
        "Grades 1-8 classes: Math, English (Grammar, includes Library Skills), Literature (Reading), Social Studies, Science (includes Health), Word Building (Spelling).",
        "To enter high school: students must have reached PACE 97 in all core subjects.",
        "To be a senior: student must have a minimum of 17 credits.",
        "Transfer students must complete at least 7 credits at HCS in order to graduate.",
        "Any student who is a cumulative amount of 50 or more PACES behind PACE level at the end of the academic year will be required to stay in the same grade in the following academic year. You will be notified if your student is approaching this level."])
    + h3("Courses of Study / Required Credits")
    + '<div class="hb-credit-grid">' + "".join(_credit_table(*prog) for prog in PROGRAMS) + "</div>"
    + h3("Early Graduation")
    + p("It is the recommendation of the administration that students complete all four years of high school with the thought that this better enables them to develop their skills and become more mature. From time to time there may be a student who, along with his/her parents/guardians, decides that early graduation is a good fit for his/her goals. The requirements are as follows:")
    + ul(["The student must submit a formal application with parental approval.",
          "Complete all PACES (through 144) in Math, English, Social Studies, Science.",
          "Complete 1 year of Bible for each year of attendance at HCS.",
          "Complete 1 year of Keyboarding and 1 year of a Foreign Language.",
          "Score 26 or higher on the ACT or 1300 on the SAT.",
          "Have approval of the School Board.",
          "Be 16 years old or older."])
    + h3("Dual Enrollment")
    + p("Upper class students may take college classes on a dual enrollment basis. The student will receive college credit and will be awarded credit by HCS. Typically, a student will receive one credit from HCS for a one semester college class of three credits or more. The credit an HCS student receives for a college class of less than three credits will be at the discretion of the School Board. The amount of HCS credit awarded for any classes students take outside of HCS will be at the discretion of the School Board.")
    + h3("Transcripts")
    + ul(["HCS will provide unofficial transcripts to students.",
          "Official transcripts will be sent directly to receiving institutions at the request of the student."])
)

CONDUCT = (
    p("Christ says that the greatest commandment is to love the Lord your God with all your heart and with all your soul and with all your mind and to love your neighbor as yourself; to love one another as He has loved us, and to do to others as you would have them do to you; to be kind to one another, tenderhearted, forgiving one another, even as God forgives.")
    + '<p class="hb-ref">Matthew 22:37, 38; Luke 6:31; John 13:34, 35; Ephesians 4:32</p>'
    + p("It is our desire to reinforce these principles in the school setting. We expect students to:")
    + ul(["<strong>Show respect</strong> to the staff and to the other students.",
          "<strong>Obey</strong> the rules with a <strong>cheerful attitude</strong>.",
          "<strong>Use good manners.</strong>",
          "Be kind to one another.",
          "Don&rsquo;t tease or provoke others.",
          "Keep <strong>hands off</strong> others. Obvious exceptions are permitted for recess games such as tag.",
          "<strong>No public display of affection</strong> between couples (i.e. hugging, holding hands, kissing)."])
    + h3("Discipline")
    + p("HCS is dedicated to the training of children in a program of study, activity, and living that is Christ-centered. We strive to teach the students that their heart attitude is of great importance to God. We evangelize them, encouraging them to love the Lord with all their heart and if they do, they will have a desire to obey. We want to encourage them and build them up in their faith and in all their godly pursuits.",
        "Every act of disobedience is an opportunity to touch the heart of the child with the grace and mercy of God as we gently approach him/her regarding his/her relationship with God, reminding him/her of how God sees his/her actions and behavior. God has shown us who know Him boundless mercy and forgiveness. We will strive to reinforce this great truth into the heart of each child.",
        "Students will be taught that though God does forgive, as well as the staff, there are consequences to sinful actions and attitudes.",
        "Our desire is that a child will change his/her attitude and/or behavior to be in line with God&rsquo;s ways; that the child will be repentant and thoughtful about his/her relationship with God and want to do what&rsquo;s right in His sight. We realize that without God&rsquo;s constant help none of us can do what He expects. So we will try to guide the students in this all-important discipline.")
    + verse("Obey them that have the rule over you, and be submissive, for they watch out for your souls, as those who must give account. Let them do so with joy and not with grief, for that would be unprofitable for you.",
            "Hebrews 13:17")
    + h3("Demerit System")
    + ul(["Demerits are given for disturbances or broken rules.",
          "The Learning Center is a study area. Students must be able to concentrate on their work. They need to be considerate of one another and do their best to not disturb and cause distractions that will inhibit others from accomplishing their goals.",
          "Three or more demerits in one day result in detention after school the next school day."])
    + h3("Detention")
    + ul(["A Detention Slip is sent home with the students. It is to be signed by a parent/guardian and returned on the next day of school.",
          "Students may be given a consequence by the supervisor relating to their conduct or attitude.",
          "Students may sit in their offices with no talking; they may do homework."])
    + '<div class="hb-scale"><h4>Detention length</h4><ul>'
    + "".join(f"<li><span>{d} demerits</span><span>{m}</span></li>" for d, m in
              [("3", "20 min"), ("4", "30 min"), ("5", "45 min"), ("6", "60 min")])
    + "</ul></div>"
    + p("When students accumulate three hours of detention in a week, they are automatically placed on probation. Probation results in the loss of privileges and extracurricular activities until the problem is corrected. The accumulation of many demerits is an indication that a student may need to be given direction in the development of godly character in his/her life. Conferences with the supervisor, administrator, and parents/guardians may be necessary to assure this growth.",
        "Demerits are recorded on a daily basis; a cumulative record is maintained. However, if less than 15 demerits are received in one quarter, the student&rsquo;s record will be erased clean with a fresh start for the next quarter. Students who receive 150 demerits will be placed on probation (i.e. no sports, extracurricular activities, privileges, etc.) and will have to meet with the School Board as a reminder that they are in danger of further serious discipline. Students who accumulate 250 demerits during the school year will be dismissed from school for the remainder of the year. Acceptance to school the following year will be at the discretion of the School Board. Parents/Guardians are notified at each 25 demerits.")
    + h3("Offenses for Which Demerits Will Be Given")
    + p("This list is to be treated as a page of examples and is not to be considered all-inclusive.")
    + '<div class="hb-offences">'
    + f"""<div><h4>1 Demerit</h4>{ul(["Homework slip not returned", "Homework slip not signed", "Incomplete homework (per PACE)", "Minor scoring violations", "Consistently not setting goals", "Unauthorized goal change", "Deviation from following the order of accomplishing goals without permission", "Detention slip not returned", "Detention slip not signed", "Being in off-limits areas", "Writing or passing notes", "Calling other students names", "Personal appearance violation", "&lsquo;Hands Off&rsquo; rule violation", "Public display of affection", "Asking a staff member permission after refusal already given by another", "Talking at testing table", "Unexcused tardy"])}</div>"""
    + f"""<div><h4>3 Demerits</h4>{ul(["PACES left home", "Monthly Scripture memory unfinished", "Throwing dangerous objects", "Unsuitable personal property", "Disrespect towards staff (includes sassing, etc.)", "Complaining", "Cheating"])}</div>"""
    + f"""<div><h4>6 Demerits</h4>{ul(["Fighting", "Lying", "Cursing / vulgar language", "Rudeness", "Blatant disobedience"])}</div>"""
    + "</div>"
    + '<div class="hb-offences hb-offences--two">'
    + f"""<div><h4>In-House Suspension</h4>{ul(["Over 6 demerits in one day", "Cheating on exams", "Fighting &mdash; 2nd violation", "Lying &mdash; 2nd violation", "Cursing &mdash; 2nd violation"])}</div>"""
    + f"""<div><h4>Expulsion</h4>{ul(["Moral impurity", "Drug use", "Alcohol use", "Smoking", "Gambling", "Repeated in-house suspension (School Board discretion)"])}</div>"""
    + "</div>"
    + h3("Discipline Terms")
    + dl([
        ("Demerit", "Mark given for violation of the rules."),
        ("Detention", "Time served after school for 3 or more demerits."),
        ("In-House Suspension", "Removal from classroom and break times; supervised work with staff member."),
        ("Probation", "Loss of privileges and extracurricular activities for a time; extra requirements may be set on goals and behaviors."),
        ("Suspension", "Removal from school for a period of time determined by administration."),
        ("Dismissal", "Removal from school with the opportunity for return."),
        ("Expulsion", "Removal from school without the opportunity for return."),
    ])
    + note("HCS reserves the right to suspend or expel a student for just cause.")
)

APPEARANCE = (
    verse("Man looks on the outward appearance, but the Lord looks on the heart.", "I Samuel 16:7")
    + p("Since we dress according to the function we are attending, we&rsquo;ve implemented the following levels of Personal Appearance Requirements in order to alleviate confusion (e.g. you wouldn&rsquo;t wear a three-piece suit to a summer barbecue, nor would you wear shorts and a T-shirt to a funeral).",
        "We expect students to maintain modesty in dress, hairstyle, and grooming. We encourage students to gain recognition through conscientious work and exemplary manners rather than in extremes of dress and behavior.",
        "Our major goal in requiring modesty in dress for our students is to protect our young men and young ladies. We want our young ladies to be viewed as sisters in Christ and treated with respect by our young men (their brothers in Christ). Because of the way young men can be tempted to sinful thoughts and desires by what they see, we ask that young ladies be considerate and present themselves in such a way that the young men will treat them with the grace and respect they deserve without being distracted by appearances.")
    + h3("School Personal Appearance Requirements")
    + ul(["This is the general day-to-day dress in the classroom and all school functions unless otherwise notified by the administration; to be followed throughout the entire school day, including arrival and departure.",
          "Students are to be respectful and compliant regarding changes he/she is requested to make.",
          "In the case of an extreme immodesty issue that cannot be readily corrected by the student, parents/guardians will be called to help correct violations. The student will not be allowed to stay in the Learning Center until dressed according to stated policy."])
    + '<div class="hb-two">'
    + f"""<div><h4>Girls</h4>{ul(["As much as possible, a female staff member will inform girls if improperly dressed.", "Clothing must be modest, neat, clean and in good repair. There can be no rips, cuts, holes or frayed edges in ANY clothing.", "Not allowed: clothing that is see-through or too tight, extra-long belts, chains, body piercing, body art or Gothic dress. Whether a student is standing or sitting or arms fully extended above the head, no skin can be showing in the midsection. Once a student is accepted for admission, a student may not get a tattoo &mdash; real or imitation &mdash; prior to graduation.", "Pants must be loose fitting dress pants. No Lycra or spandex, no tapered legs, no visible underwear line. If a student is unable to unzip/unbutton pants, we request they wear pants with an elastic waist. Pants should come to the ankle and rest securely on hips. Not allowed: jeans, capris, gauchos, pajama-like pants, low rise pants, pants with holes.", "Skirts, jumpers and dresses must come to the top of the knee cap at all points whether sitting or standing, no openings above the knee, no visible underwear lines.", "Tops must have necklines no lower than 1&Prime; below the clavicle and should cover the midsection with arms fully extended above the head. Graphic t-shirts are not allowed. No sleeveless tops.", "Layers worn over tops must be clean and in good repair, with no rips, cuts, holes, frayed edges or logos over 2&Prime; in diameter. A top as described above must be under these layers. Examples include sweaters, jackets, sweatshirts, hoodies and flannel shirts.", "Any Hartland Christian School gear can be worn as a layer regardless of the size of the graphic.", "Dress shoes or sneakers are to be worn at all times; sandals are not permitted; toes and heels must be covered for safety. Heels must be no higher than 2.5&Prime; for safety. Only sneakers are allowed on the gym floor.", "Hair must be neat and clean, no extreme styles or unnatural hair color.", "Fingernails should be neat and clean.", "Hoop earrings must be smaller than a dime for safety. Only two earrings per ear is allowed.", "Make-up and nail polish must be moderate and neat.", "No hats or hoods can be worn over the head at school."])}</div>"""
    + f"""<div><h4>Boys</h4>{ul(["As much as possible, a male staff member will inform boys if improperly dressed.", "Clothing must be modest, neat, clean and in good repair. There can be no rips, cuts, holes or frayed edges in ANY clothing.", "Not allowed: clothing that is see-through or too tight, extra-long belts, chains, body piercing, body art or Gothic dress. Whether a student is standing or sitting or arms fully extended above the head, no skin can be showing in the midsection. Once a student is accepted for admission, a student may not get a tattoo &mdash; real or imitation &mdash; prior to graduation.", "Pants must be of a solid color, cotton or cotton blend, Dockers type, chino, cotton twill, cargo or knit dress slacks. Not allowed: jeans or tapered leg pants. If a student is unable to unzip/unbutton pants, we request they wear pants with an elastic waist.", "Tops must be a collared shirt &mdash; Polo type shirt or a button up shirt of a solid color, striped or checkered. Only the top button may be unbuttoned.", "Layers worn over tops must be clean and in good repair, with no rips, cuts, holes, frayed edges or logos over 2&Prime; in diameter. A top as described above must be under these layers. Examples include sweaters, jackets, sweatshirts, hoodies and flannel shirts.", "Any Hartland Christian School gear can be worn as a layer regardless of the size of the graphic.", "Dress shoes or sneakers are to be worn at all times with socks; sandals are not permitted; toes and heels must be covered for safety. Only sneakers are allowed on the gym floor.", "Haircuts must be traditional and tapered with no sudden change in length, off from the ears and neck and cut back from the eyes. No extreme styles with shaved heads, stripes, chopped cuts or unnatural hair color. Hair should be neat and clean.", "No facial hair.", "Fingernails should be neat and clean.", "No hats or hoods can be worn over the head at school."])}</div>"""
    + "</div>"
    + h3("Business Personal Appearance Requirements")
    + p("For performances for the church, certain school programs and various other events. You will be notified in writing when this is required. Follow the School Personal Appearance Requirements in addition to these stipulations.")
    + '<div class="hb-two">'
    + f"""<div><h4>Boys</h4>{ul(["Pressed pants of a solid color &mdash; Dockers, chino, cotton twill or dress pants", "Belt", "Dress shirt", "Tie", "Dress shoes", "Dress socks"])}</div>"""
    + f"""<div><h4>Girls</h4>{ul(["Dress or skirt", "Solid coloured top", "Solid coloured socks/tights or hose", "Dress shoes"])}</div>"""
    + "</div>"
    + h3("Casual Personal Appearance Requirements")
    + p("This dress will be permitted for certain fun days and field trips as the situation warrants. You will be notified in writing when this is permitted. Permitted for volleyball and basketball games for students who are not on the team. Follow the School Personal Appearance Requirements in addition to these stipulations.")
    + ul(["T-shirts and/or sweatshirts. Character, cartoon and sports team shirts are permitted, however any writing or cartoon character considered vulgar or obscene will not be permitted.",
          "Pants, including jeans (no low riding pants)."])
    + h3("Sports Practice Personal Appearance Requirements")
    + p("Follow the School Personal Appearance Requirements in addition to these stipulations.")
    + ul(["Loose fitting athletic pants or knee-length athletic shorts.",
          "Loose fitting T-shirts or sweatshirts.",
          "Undergarments should not be seen over the tops of the outer shorts."])
)

FEES = (
    fee_rows([
        ("Tuition", "$2,600"),
        ("Convention Fee", "$250"),
        ("Art Fee", "$100"),
        ("Graduation Fee <small>12th grade</small>", "$100 <small>per student</small>"),
        ("Hot Lunch Fee", "$180"),
    ])
    + h3("Home Schooler Fees")
    + fee_rows([
        ("Arts &amp; Activities", "$55 <small>per student, per semester</small>"),
        ("Sports", "$150 <small>per student, per sport</small>"),
    ])
    + h3("Late Fees")
    + fee_rows([("Late payment", "$25.00 <small>per billing cycle</small>")])
    + note("Mandatory parent and School Board meeting after two or more months delinquency in tuition payments.", "Please note")
    + h3("New Student Fees")
    + fee_rows([
        ("Academic Testing Fee <small>grades 1-12</small>", "$75.00 <small>per student</small>"),
        ("Registration Fee <small>first student</small>", "$150"),
        ("Registration Fee <small>each additional student</small>", "$50"),
    ])
    + h3("Discounts")
    + p("If the entire tuition bill (excluding all fees) is paid in full by the first (September 15th) billing cycle, a 10% discount over the entire applicable tuition will be applied.")
    + h3("Policies")
    + p("HCS places a high value on maintaining a good testimony with its creditors. Therefore, we ask that you help us be able to keep our financial commitments by paying your tuition bills and fees faithfully and in a timely manner.",
        "Your tuition obligation will be mailed to you each month over a ten-month period from August to May. Statements will be mailed out on the first week of the month, and the due date will be the end of the month. If the due date is missed, a $25.00 late fee will be added to the next month&rsquo;s statement. Final payment is due prior to the last day of school.",
        "We understand that from time-to-time true financial hardships occur. If you know that your remittance is going to be late, please call the school immediately so that arrangements can be discussed with the school board. If a payment is missed and no contact is made with the school, then you may be asked to withdraw your child from school until such time as you are financially able to resume tuition payments.",
        "Unless prior arrangements have been made, students with unpaid tuition and/or fee balances at the end of a semester may not be allowed to return to HCS the next semester until such time as the balance is paid in full. HCS will not release transcripts until all financial obligations are met. HCS Seniors will not receive diplomas until all financial obligations are met.")
)

RECONCILIATION = (
    p("We are sons and daughters of Adam and Eve and therefore prone to sin and conflict.",
      "When the occasion arises that we need to settle differences with one another, let&rsquo;s do it in a spirit of goodwill and a desire to follow Christ&rsquo;s example, with an attitude of humility and forgiveness. Let&rsquo;s refrain from gossip, backbiting and other sins of the tongue, remembering that")
    + verse("Whoever guards his mouth keeps his soul from troubles.", "Proverbs 21:23")
    + h3("Conflicts")
    + p("When conflicts arise, we encourage you to follow the instruction of our Lord from Matthew 18 and talk directly with the people involved. Let&rsquo;s discuss our problems in a gentle manner, not provoking one another, but instead, in a spirit of love and mercy, forgiving one another, even as God for Christ&rsquo;s sake has forgiven us.")
    + h3("Grievance Procedures")
    + p("When a parent/guardian has a grievance regarding decisions made by the school, we request that you follow this chain:")
    + ol(["Talk directly with the <strong>Supervisor</strong>. Please do not discuss your grievance with the Monitors, since they are acting on behalf of the Supervisor.",
          "If you are still not satisfied, please talk with the <strong>Administrator</strong>.",
          "If you are still not satisfied, please talk with the <strong>School Board</strong>."])
    + h3("Complaints About Policies")
    + p("We request that parents/guardians encourage their children to follow policies of the school without complaining (Philippians 2:14). We have reasons for each policy. Please direct questions concerning policies to the Administrator.")
    + h3("Student Disclosure Policy")
    + p("<strong>Illegal / immoral activity.</strong> When Student A knows that Student B is contemplating or is involved in illegal or immoral activity, we encourage Student A to talk with Student B, reminding Student B of his/her commitment to Christ. If Student B continues in his/her involvement in such an activity, then Student A should notify the Administrator.")
    + note("If you think you know of a situation that is going to lead to harm, to either yourself or another student, report this to the Administrator, Supervisor or Monitor immediately.", "Important")
)

# id, contents label, heading, body
SECTIONS = [
    ("introduction", "Introduction", "Introduction", INTRO),
    ("purpose", "Purpose &amp; Objective", "Purpose and Objective", PURPOSE),
    ("admissions", "Admissions", "Admissions", ADMISSIONS),
    ("attendance", "Attendance", "Attendance", ATTENDANCE),
    ("general", "General Information", "General Information", GENERAL),
    ("extracurricular", "Extra-Curricular", "Extra-Curricular Activities", EXTRA),
    ("curriculum", "Curriculum", "Curriculum", CURRICULUM),
    ("order-of-the-day", "Order of the Day", "Order of the Day", ORDER),
    ("daily-procedures", "Daily Procedures", "Daily Procedures", DAILY),
    ("responsibilities", "Responsibilities &amp; Privileges", "Responsibilities and Privileges", RESPONSIBILITIES),
    ("courses", "Courses", "Courses", COURSES),
    ("conduct", "Conduct &amp; Discipline", "Conduct and Discipline", CONDUCT),
    ("appearance", "Personal Appearance", "Personal Appearance Requirements", APPEARANCE),
    ("fees", "Tuition &amp; Other Fees", "Tuition and Other Fees", FEES),
    ("reconciliation", "Reconciliation", "Reconciliation Procedures", RECONCILIATION),
]
