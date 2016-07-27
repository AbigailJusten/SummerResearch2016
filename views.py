from django.shortcuts import render
from jobdata.models import AllJobDataFinal, Topics

def index(request):
	return render(request, 'jobdata/index.html')

def data(request):
	data = AllJobDataFinal.objects.all()
	return render(request, 'jobdata/data.html', {'data': data})

def datadetail(request, id):
	data = AllJobDataFinal.objects.get(id=id)

	topic1_p = data.topic1_position
	topic1 = Topics.objects.get(id = topic1_p)
	data.topic1 = int(data.topic1*100)
		
	try:
		topic2_p = data.topic2_position
		topic2 = Topics.objects.get(id = topic2_p)
		data.topic2 = int(data.topic2*100)
	except (TypeError, AttributeError, Topics.DoesNotExist):
		topic2 = None
		topic2_p = None
	
	try:
		topic3_p = data.topic3_position
		topic3 = Topics.objects.get(id = topic3_p)
		data.topic3 = int(data.topic3*100)
	except (TypeError, AttributeError, Topics.DoesNotExist):
		topic3 = None
		topic3_p = None
	
	return render(request, 'jobdata/datadetail.html', {'data': data, 'topic1': topic1, 'topic2': topic2, 'topic3':topic3})

def topics(request, position):
	
	position = float(position)
		
	try:
		topic1_data = AllJobDataFinal.objects.filter(topic1_position =position)
		for topic in topic1_data:
			topic.topic1 = int(topic.topic1*100)
	except AllJobDataFinal.DoesNotExist:
		topic1_data = None

	try:
		topic2_data = AllJobDataFinal.objects.filter(topic2_position = position)
		
		for topic in topic2_data:
			topic.topic2 = int(topic.topic2*100)
	except AllJobDataFinal.DoesNotExist:
		topic2_data = None

	try:
		topic3_data = AllJobDataFinal.objects.filter(topic3_position = position)
		for topic in topic3_data:
			topic.topic3 = int(topic.topic3*100)
	except AllJobDataFinal.DoesNotExist:
		topic3_data = None
	
	topic = Topics.objects.get(id = position)

	return render(request, 'jobdata/topics.html', {'topic1_data':topic1_data, 'topic2_data':topic2_data, 'topic3_data':topic3_data, 'topic_position': position, 'topic': topic})

def topiclist(request):
	topics = Topics.objects.all()
	return render(request, 'jobdata/topiclist.html', {'topics': topics})


def jobsearch(request):
	jobtitle = request.GET.get('job')
	jobs = AllJobDataFinal.objects.filter(title__contains = jobtitle)
	return render(request,'jobdata/jobsearch.html',{'jobs': jobs})
		
def topicsearch(request):
	topic = request.GET.get('topic')
	topics = Topics.objects.filter(topic__contains = topic)
	return render(request,'jobdata/topicsearch.html',{'topics': topics})


