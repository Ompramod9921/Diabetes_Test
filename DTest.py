import streamlit as st
from streamlit_pages.streamlit_pages import MultiPage
import time

def main():
    st.image('Diabetes Quiz.png',width=700)

def sec():
    st.title('QUIZ : Are You at Risk for Diabetes ?')
    st.image('https://images.pexels.com/photos/6823763/pexels-photo-6823763.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',width=700)
    st.markdown(f"**There are three major types of disease: type 1, type 2, and gestational diabetes. With all three, your body can't make or use insulin. One of every four people with diabetes doesn't know they have it. Are you at risk? Diabetes is a manageable condition, but left untreated it can cause serious harm. Try our quiz to see if you are showing any of the tell-tale signs.**")
    st.success('''Who is this quiz for ? >>>> If you're concerned that you might be experiencing some of the symptoms of diabetes, or know that you may be at risk of the condition, this quiz should help you discover whether you are exhibiting some of the symptoms and evaluate your risk . ''')
    st.warning('''Who is at risk ? >>>> Type 1 diabetes is an autoimmune condition and as yet the triggers for this condition are unknown. However, type 2 diabetes has a number of risk factors, including being overweight or obese, living a sedentary lifestyle, or eating an unhealthy, high-calorie diet. "With type 2 diabetes your body's still producing at least some insulin (which helps our cells to utilise glucose) but you can't respond to it - you've lost that sensitivity. If the system gets overworked - eating the wrong things, eating too frequently, too much - the system gets worn out and we lose the sensitivity to it " , explains Dr Jenna Macciochi, Doctor of Immunology at the University of Sussex. ''')
    st.success('''Might I have diabetes and not realise ? >>>> With type 1 diabetes, the body stops producing insulin, meaning the effect on the body is usually rapid and noticeable. However, type 2 diabetes develops slowly - the body still produces insulin, but it may be insufficient, or the body might not respond to it properly. This means that the development of symptoms is gradual. "Symptoms for type 1 diabetes often develop very fast," explains Macciochi. "But with type 2 diabetes you may not even know you have it, as symptoms can be very subtle. ''')
    st.warning('''What does the test consist of ? >>>> The test consists of 15 questions, looking at symptoms you may have noticed. Using the data, you will then be given advice on whether to seek help. ''')
    st.success('''How accurate is it ? >>>> The only conclusive test for diabetes is a blood test. However, the quiz should give you an indication of whether to seek urgent help, or whether to raise the issue at your next GP appointment. ''')

def third():
    count = 0
    st.subheader(' 👇 Select suitable option')

    q1 = st.radio("1) Do you have a problem with your weight?",('Yes, I’m overweight or obese','Yes, I’ve recently experienced unexplained weight-loss','No'))
    if q1 == "No" :
        st.error('Facts...Although being overweight can be a risk factor for type 2 diabetes, and losing weight unexpectedly might be a symptom of type 1 diabetes, these are not definitive symptoms of the condition.')
    elif q1 == 'Yes, I’m overweight or obese':
        count += 0.25
        st.error('Facts...Being overweight can predispose you to type 2 diabetes, so having excess weight may make you more likely to have the condition. Conversely, unexplained weight loss can be a symptom of type 1 diabetes. This is because the body is unable to metabolise sugar and may start breaking down fat.')
    else :
        count += 0.25
        st.error('Facts...Being overweight can predispose you to type 2 diabetes, so having excess weight may make you more likely to have the condition. Conversely, unexplained weight loss can be a symptom of type 1 diabetes. This is because the body is unable to metabolise sugar and may start breaking down fat.')
    
    q2 = st.radio("2) Have you felt thirstier, or found yourself drinking water more than usual in recent weeks or months?",('Yes','No'))
    if q2 == 'Yes' :
        count += 0.25
        st.error('Facts...Increased thirst is a symptom of both types of diabetes and is caused by your body’s inability to process the sugar in your blood. Instead, your body takes fluid from your body to try to dilute the sugar, causing thirst.')
    else :
        st.error('Facts...Whilst thirst can be a symptom of diabetes, this symptom can come on gradually. With type 2 diabetes, you don’t lose the ability to process sugar overnight, meaning the onset of excess thirst may be so gradual that you don’t notice it.')

    q3 = st.radio("3) Are you peeing more than usual?",("Yes – I seem to go a lot more often than anyone else!","No, I don’t think so"))
    if q3 == "Yes – I seem to go a lot more often than anyone else!" :
        count += 0.25
        st.error("Facts...Alongside excess thirst, going to the toilet more often can be a symptom of diabetes. This is partly due to the fact you may be drinking more and partly because your body may be secreting excess sugar in the urine. However, an increased frequency in peeing could also be a symptom of other conditions, including urinary tract infection. Make sure you mention this symptom when you next speak to your doctor.")
    else :
        st.error("Facts...More frequent peeing is a symptom of diabetes, but not everyone experiences the same symptoms. In addition, this symptom can come on gradually, meaning you might not notice the increase.")

    q4 = st.radio("4) Have you noticed that any cuts and grazes you might have seem to be taking longer to heal than usual?",('No, they are healing just fine','Yes, they seem to be taking longer') )
    if q4 == "No, they are healing just fine" :
        count += 0.25
        st.error('Facts...Glucose levels in the bloodstream caused by diabetes may cause poor circulation, and slow down healing. However, those who have just developed diabetes may not yet have experienced this symptom.')
    else :
        st.error('Facts...Diabetes causes levels of blood glucose to rise, which can lead to poor circulation. This means if you cut yourself, it can be harder for the blood to reach the area affected in order to repair it. However, slow wound healing can also happen as a result of ageing, or of other conditions including zinc deficiency.')

    q5 = st.radio("5) Have you noticed any changes to your vision?",('Yes, I seem to have trouble with my focus sometimes','Yes, I sometimes see ‘floaters’ in my line of vision','Yes, sometimes my eyesight seems a little blurry','No, my eyes are fine'))
    if q5 == 'No, my eyes are fine' :
        st.error('Facts...Diabetes can cause problems with vision; however, early stage diabetic retinopathy may be asymptomatic. If you are experiencing other symptoms of diabetes, it’s important to speak to your GP.If you get a sudden increase in "floaters", you should seek urgent medical help as there are other possible causes that could threaten your eyesight if untreated.')
    else :
        if q5 == 'Yes, I seem to have trouble with my focus sometimes' :
            count += 0.75
            st.error('Facts...Diabetes can cause problems with vision; however, early stage diabetic retinopathy may be asymptomatic. If you are experiencing other symptoms of diabetes, it’s important to speak to your GP.If you get a sudden increase in "floaters", you should seek urgent medical help as there are other possible causes that could threaten your eyesight if untreated.')
        elif q5 == 'Yes, I sometimes see ‘floaters’ in my line of vision' :
            count += 0.50
            st.error('Facts...Diabetes can cause problems with vision; however, early stage diabetic retinopathy may be asymptomatic. If you are experiencing other symptoms of diabetes, it’s important to speak to your GP.If you get a sudden increase in "floaters", you should seek urgent medical help as there are other possible causes that could threaten your eyesight if untreated.')
        else :
            count += 0.25
            st.error('Facts...As diabetes worsens, the build-up of glucose in the blood can cause complications in blood vessels. In some cases, this may lead to eye problems, which, if left untreated, can lead to blindness. Early symptoms include trouble with focus, seeing "floaters" in the field of vision or having blurred vision. However, vision problems are not necessarily a sign of diabetes, as it is common for our vision to deteriorate as we age.If you get a sudden increase in "floaters", you should seek urgent medical help as there are other possible causes that could threaten your eyesight if untreated.')


    q6 = st.radio("6) Have you experienced recent tingling or a pins and needles sensation in the hands or feet?",('No','Yes, once or twice','Yes, frequently'))
    if q6 == 'No' :
        st.error('Facts...Diabetes can lead to tingling in the hands and feet caused by inflammation of blood vessels. However, these symptoms can take several years to start after you develop diabetes. Not having this symptom is a good sign – but not conclusive on its own.')
    else :
        if q6 == 'Yes, once or twice' :
            count += 0.25
        else :
            count += 0.50
        st.error('Facts...As well as affecting the vessels in the eyes, high levels of glucose in the bloodstream can lead to an inflammatory response. As this frequently occurs in the smaller vessels, it can cause diabetic neuropathy – tingling in the hands and feet. This inflammatory response may also lead to cardiovascular disease, so if you have any concerns make sure you get checked out. However, as with many symptoms, there can be other causes of tingling in the extremities, including poor circulation, vitamin or mineral deficiency and panic attacks.')

    q7 = st.radio("7) Have you been experiencing excessive tiredness or fatigue?",('No, I feel the same as always','Yes, I’m exhausted!','I’m a little more tired than usual'))
    if q7 == 'No, I feel the same as always' :
        st.error('Facts...People with diabetes often feel tired due to problems with circulation. This is a common symptom of diabetes, so if you aren’t experiencing this problem, that’s good news! However, if you are exhibiting other signs of diabetes, you need to speak to your GP.')
    else :
        if q7 == 'Yes, I’m exhausted!':
            count += 0.50
        else :
            count += 0.25
        st.error('Facts...Slow circulation in diabetes can mean that your body isn’t delivering sufficient oxygen to your cells, making you feel more tired. Tiredness can also occur due to inflammation may cause monocytes – large white blood cells - to enter the brain. However, feeling tired can be a symptom of many conditions, including having an underactive thyroid, depression and poor sleep.')

    q8 = st.radio("8) Do you have a mother, father, sister, or brother with diabetes?",('Yes','No'))
    if q8 == 'Yes':
        count += 0.25
    st.error('Facts...A family history of diabetes could contribute to your risk for type 2 diabetes .There’s a link between family history and type 2 diabetes, but not only because family members are related. Sometimes they share certain habits that can increase their risk.')

    q9 = st.radio("9) Have you ever been diagnosed with high blood pressure?",('Yes','No'))
    if q9 == 'Yes':
        count += 0.25
    st.error('Facts...Having high blood pressure contributes to your overall risk for type 2 diabetes.It can also increase your risk for heart disease, eye problems, and kidney disease or make them worse.')

    q10 = st.radio("10) How old are you?",('Younger than 40','40-49 Years','50-59 Years','60+ Years'))
    if q10 == '40-49 Years':
        count += 0.25
    elif q10 == '50-59 Years':
        count += 0.50
    else :
        count += 0.75
    st.error('Facts...You are at a higher risk for type 2 diabetes the older you are.Risk starts to increase at around age 45 and increases sharply after age 65.')

    q11 = st.radio("11) Are you physically active?",('Yes','No'))
    if q11 == 'Yes' :
        count += 0.25
    st.error('Facts...Being inactive can increase your risk for type 2 diabetes.One reason is that your body can’t use insulin as well when you don’t get regular physical activity. Insulin helps keep blood sugar levels from getting too high.')
    
    q12 = st.radio("12) Do you have a low level of HDL 'good' cholesterol?",('No','Yes') )
    if q12 == 'Yes' :
        count += 0.25
    st.error('Facts...Observationally, low levels of HDL cholesterol are consistently associated with increased risk of type 2 diabetes.')
    
    q13 = st.radio("13) Do you have a high level of triglycerides?",('Yes','No'))
    if q13 == 'Yes' :
        count += 0.25
    st.error('Facts...Having high triglycerides - a type of fat in the blood - may be a sign you may have prediabetes or type 2 diabetes.')
    
    q14 = st.radio("14) Are you a man or a woman?",('Man','Woman'))
    st.error("Facts...Men are more likely than women to have undiagnosed diabetes; one reason may be that they are less likely to see their doctor regularly.")
    if q14 == 'Woman' :
        q14W = st.radio("15) Have you ever been diagnosed with gestational diabetes?",('Yes','No'))
        if q14W == "Yes" :
            count += 0.25
        st.error('Facts...Gestational diabetes is a type of diabetes that develops during pregnancy. It goes away after pregnancy, but women who have gestational diabetes have an increased risk of developing type 2 diabetes.')
    else:    
        count += 0.25

    if st.button('submit'):
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.05)
            my_bar.progress(percent_complete + 1)
        if count <= 2 :
            st.image('https://images.pexels.com/photos/6836350/pexels-photo-6836350.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',width=700)
            st.error('Your risk of diabetes is low')
            st.success('''Based on your results, you’re at low risk for prediabetes. Keep up the good work! These healthy habits will help keep your risk low:
                        Get at least 150 minutes of physical activity a week.
                        Keep your weight in a healthy range.
                        Eat healthy foods, including lots of fruits and veggies.
                        Drink more water and fewer sugary drinks.
                        Don’t smoke.
            Your results indicate that you probably don’t have diabetes. However, as this condition can come on slowly – and many of the symptoms may go unnoticed - make sure to raise any concerns with your GP.''')
        elif 2 < count <= 3.5 :
            st.image('https://images.pexels.com/photos/6836421/pexels-photo-6836421.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',width=700)
            st.error('Your risk of diabetes is moderate')
            st.success('You are displaying some of the symptoms of diabetes. Speak to your GP at your next appointment: they will send you for a blood test if required.')
        elif 3.5 < count <= 4.5 :
            st.image('https://images.pexels.com/photos/6836393/pexels-photo-6836393.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',width=700)
            st.error('Your risk of diabetes is high')
            st.success('Based on your score, you’re likely to have prediabetes, but only your doctor can diagnose it for sure.No quiz can tell you whether you have a specific condition. However you are displaying many of the symptoms of diabetes. It’s important that you speak to your GP as soon as possible, and if necessary, get tested for the condition.')

def four():
    st.markdown('# Diabetes? Yoga to the Rescue ')
    st.image('yoga.jpg',width=730)
    st.markdown(f"**Study after study at top Western universities confirm and reiterate what our ancient science has been preaching all along -that positive health effects of yoga are bountiful.**")
    st.markdown(f"**In fact, a study published in the journal, Evidence-Based Complementary and Alternative Medicine, last year analysed available research looking at yoga's influence on diabetes and complications of diabetes (for instance, kidney problems and high blood pressure) and found that regular yoga practise led to shortterm improvements in fasting glucose and cholesterol levels. The research, conducted by Marshall Govindan and Dr Emilia RipollBunn, also found that the direct stim ulation of the pancreas by certain postures rejuvenated its capacity to produce insulin.**")
    st.markdown(f'**Yoga therapist Shobha Honnakore adds, “A few asanas help balance the functioning of the endocrine system.It massages and tones the abdominal organs like pancreas and liver, stimulate the nervous and circulatory system which in turn helps in controlling diabetes ."**')
    st.markdown(f'**Studies have also confirmed that practising certain asanas such as Ardha Matsyendrasana (half-twist pose) combined with Dhanurasana (bow pose), Vakrasana (twisted pose), Matsyendrasana (half-spinal twist), Halasana (plough pose) squeezes and compresses the abdomen and helps stimulate the pancreatic secretions or hormonal secretions. As a result, more insulin is pushed into the system. This rejuvenates the insulin producing beta cells in the pancreas of diabetics suffering from both type 1 and 2. Practising the postures in a relaxed manner, without exertion, meditation and breathing techniques help most patients control the triggers or causes of diabetes.**')
    st.markdown(f'**The best yoga for beginners with diabetes includes postures and breathing exercises that are designed specifically to target and stimulate the pancreas. By improving blood flow to the pancreas, yoga postures for diabetes rejuvenate the organ’s cells and improve its ability to produce insulin for the body.**')
    st.markdown('## How yoga can help fight diabetes')
    st.write('''The diagnosis of Diabetes can be overwhelming and to be honest quite 
scary, luckily whether you are in advanced stages of the disease or have 
just been diagnosed, doctors and health experts have found that simple 
lifestyle choices can help to control, and even reverse the symptoms.''')
    st.warning("Health of the Nervous System :")
    st.info('''People with diabetes are at risk of developing problems with autonomic 
nervous system, which are the nerves that you can‘t consciously control. 
Problems that can arise from this are anything from bowel movements to 
the regulation of heart rate and blood pressure. It can also affect the 
peripheral nervous system, leading to reduced movement and sensation, 
or numbness. First in the feet and later into the hands. Many asanas 
(postures) in yoga, particularly back bending help to remove blockages 
from your central nervous system (running up the spine), this can 
improve the functioning of the autonomic nervous system and 
preliminary evidence (see the link
http://www.ncbi.nlm.nih.gov/pubmed/12613392) suggests it can improve 
nerve conduction.''')
    st.warning('Massaging the Internal organs:')
    st.info('''In the same way that you might find yourself rubbing your achy muscles 
after lots of physical exertion, particular postures can press or massage 
the internal organs. This increases blood flow to the area bringing more 
oxygen. Postures (particularly the twisting postures) compresses the abdomen 
against the thigh and induces stomach breathing, as a result the internal 
organs (kidneys, liver, pancreas etc.) are massaged, speeding up the 
blood circulation and cleansing effect (removal of toxins, blood is the 
carrier of the toxins as well as the nutrients).
Similarly massaging of the pancreas will happen which will rejuvenate it 
and increase the production of the pancreatic cells and the insulin. This is 
how yoga differs from other forms of exercises.''')
    st.warning('Stress Reduction :')
    st.info('''Stress is a major contributing factor to diabetes. When we are stressed it 
increases the secretion of glucagon, which is responsible for increasing 
the blood glucose levels. Stress also releases cortisol, adrenaline, which 
can trigger food cravings. If you can consistently take a few minutes a 
day to practice a combination of the yoga asanas (postures), pranayama 
(breathing exercised), and meditation or just taking time out to calm 
down, you will help to reduce stress in the mind and body. It will help 
you to make healthier choices in all aspects of your life.''')
    st.warning('Weight loss & lower blood pressure :')
    st.info('''Diabetes symptoms often get worse with high blood pressure, (or 
hypertension).High intensity sequences like the Surya Namaskar (sun salutation) can 
help to reduce weight and extra fat, which in turn will keep the blood 
pressure in check.''')
    st.warning('Lowers the blood sugar level: ')
    st.info('''As explained earlier, the various postures of Yoga massage the internal 
organs and increase the insulin sensitivity helping to decrease the blood 
sugar level. Also sequences like Surya Namaskar (Sun Salutations) will 
burn the glucose and the fats decreasing the sugar level in the body''')
    st.markdown('## Yoga poses for diabetes')
    st.subheader('Pose #1: Bhujangasana or Cobra Pose')
    st.image('https://media.gettyimages.com/photos/stretching-is-something-you-should-be-doing-every-day-picture-id1282295345?k=20&m=1282295345&s=612x612&w=0&h=oKjjpVm4fs2l90R954mI2beWryCvj_Bt0z1a1YU-Xok=',width=730)
    st.subheader('Pose #2: Pavana Muktasana or The Wind-Free Pose')
    st.image('https://th.bing.com/th/id/OIP.yLB25rZMlK598daEFKmyyQHaE8?w=279&h=186&c=7&r=0&o=5&dpr=1.25&pid=1.7',width=730)
    st.subheader("Pose #3: Vajrasana or the Thunderbolt Pose")
    st.image('https://th.bing.com/th/id/OIP.JWURcxjxWWfexozkI0S4lgHaEL?w=327&h=184&c=7&r=0&o=5&dpr=1.25&pid=1.7',width=730)
    st.subheader("Pose #4: Tadasana or the Palm Tree Pose")
    st.image('https://th.bing.com/th/id/R.36ed0ae0c6831ac21429e50feeb9c431?rik=cEgC94SeOLw8Lg&riu=http%3a%2f%2f2.bp.blogspot.com%2f_5UdEsCydnuw%2fTELM4JkNPeI%2fAAAAAAAAAZg%2faOfpeMpKsdA%2fs1600%2f45.%2bUP%2bMOUNTAIN.jpg&ehk=PzkJelMo2FV6oe3UUZN%2fgKs3yu5OEAxR3zR%2fIwcTnRo%3d&risl=&pid=ImgRaw&r=0',width=730)

app = MultiPage()
app.add_page("Welcome",main)
app.add_page("Quiz Information",sec)
app.add_page("Take Quiz",third)
app.add_page("yoga for diabetes",four)
app.run()