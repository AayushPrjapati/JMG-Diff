import re

file_path = r'C:\Users\Aayush Prajapati\OneDrive\Desktop\Internship_Summer_2026\JMG-Diff\docs\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

colab_badge = '''
                <a href="https://colab.research.google.com/" target="_blank" class="badge badge-github" id="btn-colab" style="background-color: #f9ab00; color: white;">
                    <svg viewBox="0 0 24 24" class="icon" fill="white"><path d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.365.965 3.96.987 1.632.023 2.65-1.432 3.64-2.88 1.154-1.688 1.63-3.326 1.652-3.414-.037-.015-3.197-1.22-3.232-4.832-.027-3.027 2.47-4.475 2.584-4.542-1.41-2.062-3.606-2.28-4.275-2.324-1.78-.182-3.488 1.054-4.382 1.054a5.1 5.1 0 0 1-1.396-.164M15.42 4.606c.846-1.024 1.41-2.448 1.255-3.882-1.226.05-2.709.818-3.585 1.868-.783.917-1.455 2.378-1.267 3.784 1.365.106 2.75-.682 3.597-1.77"/></svg>
                    Try in Colab
                </a>
'''

content = re.sub(r'(Code \(GitHub\)\s*</a>)', r'\1' + colab_badge, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
