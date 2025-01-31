from helpers import commands

if __name__ == "__main__":
    print('main')
    completed = commands.run(
        'docker compose up -d'
    )
    print(completed.args)
    print(completed.returncode)
    print(completed.stdout)
    print(completed.stderr)