require 'net/http'
require 'uri'
require 'json'

class ChatGptRequest
  def request_gpt(prompt)
    url = URI.parse('https://api.openai.com/v1/chat/completions')
    data = {
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'assistant', content: prompt }]
    }
    api_key = 'your api key'
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    request = Net::HTTP::Post.new(url.path, {'Content-Type' => 'application/json',
                                             'Authorization' => "Bearer #{api_key}"})
    request.body = data.to_json

    response = http.request(request)
    json_response = JSON.parse(response.body)
    content = json_response['choices'][0]['message']['content']

    return content
  end
end

